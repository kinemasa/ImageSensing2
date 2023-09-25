"""
画像の収縮と膨張を行う
入力：画像
出力：変換結果画像
"""

import cv2
import numpy as np
import binary as bi


def MorphologyErode(img):
    img =cv2.imread(img,0)
    threshold =input("input number :")
    threshold = int(threshold)
    ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2,2),dtype=np.uint8)
    img_e = cv2.erode(img_th,kernel)
    return img_e

def Morphologydilate(img):
    img =cv2.imread(img,0)
    threshold =input("input number :")
    threshold = int(threshold)
    ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2,2),dtype=np.uint8)
    img_d = cv2.dilate(img_th,kernel)
    return img_d




if __name__ == "__main__":
    imgName  = "/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/adaptiveThreshold1010.png"
    # img_erode = MorphologyErode(imgName)
    # img_dilate=Morphologydilate(imgName)

    # cv2.imshow("erode",img_erode)
    # cv2.imshow("dilate",img_dilate)
    
     
    img = cv2.imread(imgName,0)
    img = cv2.bitwise_not(img)
    # カーネルを作成する。
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # 2値画像を収縮する。
    dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    dst = cv2.bitwise_not(dst)
    cv2.imwrite("resultopen.png",dst)

