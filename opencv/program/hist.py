"""
画像のヒストグラムを表示する

input :画像
output :画像のヒストグラム
"""

import cv2
import matplotlib.pyplot as plt

def color_hist(img):
    color_list = ["blue","green","red"]
    for i,j in enumerate(color_list):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist,color =j)
    plt.show()

def gray_hist(img):
    hist =  cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)

    plt.show()


def hist_equalization(img):
    img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ##ヒストグラム平坦化
    img_equalization = cv2.equalizeHist(img_gray)
    hist_equalization =cv2.calcHist([img_equalization],[0],None,[256],[0,256])
    plt.plot(hist_equalization)
    plt.show()


if __name__ == "__main__":
    img = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/src/gantei100.tiff")
    gray_hist(img)


