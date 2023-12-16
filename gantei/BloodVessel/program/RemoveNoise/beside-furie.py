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


  
INPUT_DIR = '/Volumes/Extreme SSD/1122/gantei10010/'
files = glob.glob(INPUT_DIR+'*')
OUTPUT_DIR= '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/result/furied/'
# temp = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/template.png")
num = len(files)

##import picture
img_name = files[0]
img = cv2.imread(img_name)
img_copy=cv2.imread(img_name)

width = int(img.shape[1])
height = int(img.shape[0])



##import picture
i = 0
for f in files:
    basename=os.path.basename(f)
    root, ext = os.path.splitext(basename)
    # import img and make apply furie function
    img = cv2.imread(f,0)
    f = np.fft.fft2(img)                        # 2Dフーリエ変換
    f_shift = np.fft.fftshift(f)                # 直流成分を画像中心に移動させるためN/2シフトさせる
    mag = 20 * np.log(np.abs(f_shift))          # 振幅成分を計算

    # 周波数領域にマスクをかける
    rows, cols = img.shape                      # 画像サイズを取得
    crow, ccol = int(rows / 2), int(cols / 2)   # 画像中心を計算
    mask = 30                    # マスクのサイズ
    # f_shift[crow-mask:crow+mask,
    #         ccol-mask:ccol+mask] = 0
    f_shift[:crow-mask,
        ccol] = 0
    f_shift[crow+mask:,
        ccol] = 0

    mag_filterd = 20 * np.log(np.abs(f_shift))

    # 2D逆フーリエ変換によりフィルタリング後の画像を得る
    f_ishift = np.fft.ifftshift(f_shift)        # シフト分を元に戻す
    img_back = np.fft.ifft2(f_ishift)           # 逆フーリエ変換
    img_back = np.abs(img_back)                 # 実部を計算する



   # plt.show()

    output_file = OUTPUT_DIR + str(i) +".png"
    cv2.imwrite(output_file,img_back)
    i += 1

    sys.stdout.flush()
    sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

i = 0


