"""
フーリエ変換を用いて画像の横縞ノイズを消す

input :眼底画像群フォルダ
output :テンプレートマッチングを行ってトリミングを行った画像群
"""

import cv2
import numpy as np
import glob
import sys
import os
import matplotlib.pyplot as plt

def make_mask(img, R, inv=False): ## True = HighPass　False Lowpass
    """円形のマスク画像を作ります"""
    height = img.shape[0]
    width  = img.shape[1]

    center_w = height//2
    center_h = width//2

    if inv:
        n = 0
        filter_matrix = np.ones([height, width])
    else:
        n = 1
        filter_matrix = np.zeros([height, width])

    for i in range(0, height):
         for j in range(0, width):
                if (i-center_w)*(i-center_w) + (j-center_h)*(j-center_h) < R*R: ## 円形フィルタ（三角関数利用）
                               filter_matrix[i][j] = n

    

    return filter_matrix

def masked_fft(img, mask):
    dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)*mask

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    magnitude_spectrum[magnitude_spectrum==-np.inf]=0

    f_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    dft2 = cv2.dft(np.float32(img_back),flags = cv2.DFT_COMPLEX_OUTPUT) #flags=cv2.DFT_COMPLEX_OUTPUT dft[:,:,0]実数, dft[:,:,1]複素数
    dft_shift2 = np.fft.fftshift(dft2)

    magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))
    # ここからグラフ表示

    return magnitude_spectrum, img_back, magnitude_spectrum2

  
# INPUT_DIR = '/Volumes/Extreme SSD/1211/DMK33UX174/tumu3/'
# files = glob.glob(INPUT_DIR+'*')
# OUTPUT_DIR= '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/result/lowfuried/'
# # temp = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/template.png")
# num = len(files)

# ##import picture
# img_name = files[0]
# img = cv2.imread(img_name)
# img_copy=cv2.imread(img_name)

# width = int(img.shape[1])
# height = int(img.shape[0])



##import picture
# i = 0
# for f in files:
#     basename=os.path.basename(f)
#     root, ext = os.path.splitext(basename)
#     img_gray = cv2.imread(f,0)
    
#     r =300## 半径の設定

#     mask = np.array([make_mask(img_gray,R=r,inv = False),make_mask(img_gray,R=r,inv =False)]).transpose(1,2,0)
#     spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray, mask)

#     output_file = OUTPUT_DIR + str(i) +".png"
#     plt.gray()
#     plt.imsave(output_file,img_ifft)
    
#     i += 1

#     sys.stdout.flush()
#     sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

# i = 0

img_gray =cv2.imread("/Users/masayakinefuchi/labo/wavelet.png",0)
r =30## 半径の設定

mask = np.array([make_mask(img_gray,R=r,inv = False),make_mask(img_gray,R=r,inv =False)]).transpose(1,2,0)
spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray, mask)

output_file = "/Users/masayakinefuchi/labo/waveletlowfurie.png" 
output_file1 = "/Users/masayakinefuchi/labo/waveletlowfurie1.png" 
plt.gray()
plt.imsave(output_file,img_ifft)
plt.imsave(output_file1,spectrum_img1)

