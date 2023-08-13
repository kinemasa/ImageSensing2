import cv2
import numpy as np


import binary as bi

"""
入力した画像から閾値を調べ　モルフォルジー変換　膨張と職掌を行う
"""
def MorphologyErode(img):
    threshold =input("input number :")
    threshold = int(threshold)
    ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2,2),dtype=np.uint8)
    img_e = cv2.erode(img_th,kernel)
    return img_e

def Morphologydilate(img,threshold):
    threshold =input("input number :")
    threshold = int(threshold)
    ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2,2),dtype=np.uint8)
    img_d = cv2.dilate(img_th,kernel)
    return img_d



if __name__ == "__main__":
    img = cv2.imread("opencv\src\ganteiBlood.png",0)
    bi.binary_threshold(img)
    img_erode = MorphologyErode(img)
    img_dilate=Morphologydilate(img,84)

    cv2.imshow("erode",img_erode)
    cv2.imshow("dilate",img_dilate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
