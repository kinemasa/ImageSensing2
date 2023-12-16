"""
血管強調を行う

morph血管強調フィルタ
等方性ウェーブレットフィルタ

input :眼底画像
output : 血管強調画像
"""

import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import rescale_intensity
import extract_green_channel as egc
import rotate_image as ri

##VesselSize : the approximate diameter of the biggest vessel in the image
def morph_reconstruct_filter(grChannel,vesselSize):

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))##特定化ヒストグラム平坦化
    
    gr = clahe.apply(grChannel)
    gr = ~gr##ビット反転
    plt.imsave("grChannel.png",gr)
    kernel = np.zeros((vesselSize,vesselSize), dtype = np.uint8)
    kernel[9,:] = np.ones((1,vesselSize), dtype = np.uint8)
    morph_image = np.zeros_like(grChannel)
    plt.imsave("morph.png",morph_image)
    for angle in range(15, 180, 180 // 12):
        image = cv2.morphologyEx(gr, cv2.MORPH_OPEN, ri.rotate_image(kernel, angle), iterations = 1)
        morph_image = cv2.add(morph_image, cv2.subtract(gr, image))
    return morph_image


##カーネルとの畳み込み処理を行う
def convolve2D(image,filter):
    (iH, iW) = image.shape
    (kH, kW) = filter.shape
    
    padding = (kW - 1) // 2
    img = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_REPLICATE)
    
    w = np.zeros((iH,iW), dtype = "float32")
    output = np.zeros((iH, iW), dtype = "float32")
    
    for y in np.arange(padding, iH + padding):
        for x in np.arange(padding, iW + padding):
            roi = img[y - padding:y + padding + 1, x - padding:x + padding + 1]
            output[y - padding,x - padding] = (roi * filter).sum()
    
    w = image - output

    output = rescale_intensity(output, in_range = (0,255))
    output = (output * 255).astype("uint8")
    return output, w


def isotropic_undec_wavelet_filter2D(image):
   
    # Bi-spline cubic function is given by h
    c_prv = image
    C1 = 1. / 16.
    C2 = 4. / 16.
    C3 = 6. / 16.
    
    W = []
    C = []
    kernel_sizes = [5,9,17]
    for idx, ks in enumerate(kernel_sizes):
        ks = ks//2
        kernel = np.zeros((1, kernel_sizes[idx]), dtype = 'float32')
        kernel[0][0] = C1
        kernel[0][kernel_sizes[idx]-1] = C1
        kernel[0][int(ks/2)] = C2
        kernel[0][int(kernel_sizes[idx]/4+ks)] = C2
        kernel[0][ks] = C3
        
      
        c_nxt, w = convolve2D(c_prv, kernel.T * kernel)
        c_prv = c_nxt
        W.append(w)
        C.append(c_prv)
        A = kernel.T * kernel


    
    #     Computing the result Iiuw
    #Iiuw = W[1] + W[2]
    Iiuw= W[1] + W[2]
    plt.gray()
    plt.imsave("wavelet-w012.png",Iiuw)
    return Iiuw, C, W


if __name__ =="__main__":
    
    ##Mac
    img ="/Users/masayakinefuchi/labo/otu.png"
    
    grChannel= egc.extract_green_channel(img)
    
    # morphChannel= morph_reconstruct_filter(grChannel,10)
    filtered_result, c, _ = isotropic_undec_wavelet_filter2D(grChannel)
    plt.gray()
    # plt.imsave("morph.png",morphChannel)
    plt.imsave("wavelet.png",filtered_result) 
    plt.imsave("c.png",c[2]) 
   