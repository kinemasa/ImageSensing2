import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import rescale_intensity

# from function import extract_green_channel as egc
# from function import rotate_image as ri

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
def convolve2D(image,kernel):
    (iH, iW) = image.shape
    (kH, kW) = kernel.shape
    pad = (kW - 1) // 2
    img = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    w = np.zeros((iH,iW), dtype = "float32")
    output = np.zeros((iH, iW), dtype = "float32")
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = img[y - pad:y + pad + 1, x - pad:x + pad + 1]
            output[y - pad,x - pad] = (roi * kernel).sum()
    
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
        A = kernel.T * kernel


    
    #     Computing the result Iiuw
    Iiuw = W[1] + W[2]
    #Iiuw= W[0]
    plt.imsave("wavelet.png",Iiuw)
    return Iiuw, c_nxt, W


if __name__ =="__main__":
    img ="gantei/BloodVessel/src/ganteiBlood.png"
    grChannel= egc.extract_green_channel(img)
    
    morphChannel= morph_reconstruct_filter(grChannel,10)
    filtered_result, _, _ = isotropic_undec_wavelet_filter2D(grChannel)
    
    # cv2.imshow("wavelet",filtered_result)
    plt.imsave("wavelet.png",filtered_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()