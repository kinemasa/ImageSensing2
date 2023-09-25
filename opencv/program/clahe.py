import numpy as np
import cv2

img = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/s.png",0)

clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))

cl1 = clahe.apply(img)
cv2.imwrite("clahe8.png",cl1)
# ノイズ除去した画像
# result = cv2.fastNlMeansDenoising(cl1, h=10)
# cv2.imshow("reslut",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()