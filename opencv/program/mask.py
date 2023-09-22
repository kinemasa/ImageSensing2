import cv2
import numpy as np


def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi
  
#返されるのはリスト[min_x、min_y、w、h]です。
# 画像を読み込み
image = cv2.imread('/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/clahe2.png')

while True:
 roi = getVideoROI(image)
 cv2.rectangle(image,
              pt1=(roi[0], roi[1]),
              pt2=(roi[0]+roi[2], roi[1]+roi[3]),
              color=(255, 255, 255),
              thickness=-1,
              lineType=cv2.LINE_4,
              shift=0)

 cv2.imshow("mask",image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
 keybordInput = input("抜ける場合はs,続ける場合はcを入力してください")
 if keybordInput == "s":
   break
 else :
   continue
