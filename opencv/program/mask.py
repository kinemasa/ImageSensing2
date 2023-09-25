import cv2
import numpy as np


def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi
  
#返されるのはリスト[min_x、min_y、w、h]です。
# 画像を読み込み
image = cv2.imread('/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/clahe8.png')

mask  = cv2.imread('/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/medianbinary.png')
mask = cv2.bitwise_not(mask)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
maskedImage = cv2.bitwise_and(image,mask)

M = np.ones(image.shape, dtype="uint8") * 50
subtracted_image = cv2.subtract(maskedImage, M)
cv2.imwrite("mask2.png",maskedImage)

 