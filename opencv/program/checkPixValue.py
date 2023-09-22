import cv2
import numpy as np
def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi
  
#返されるのはリスト[min_x、min_y、w、h]です。
# 画像を読み込み
image = cv2.imread('/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/clahe2.png')
roi = getVideoROI(image)
num = len(roi)
width,height= roi[2],roi[3]
print(width,height)
pixArray = []
i =0
for h in range(height):
  for w in range (width):
    x =roi[0]+w
    y =roi[1]+h
    
  # # RGBの各チャンネルのデータを一度に取得
    pixel = image[x, y]
    pixelValue = image[x, y, 0]
    pixArray.append(pixelValue)
    
    i+=1
    
print(i)

#numpy.median関数を用いる。
median = np.median(pixArray)

for h in range(height):
  for w in range (width):
    x =roi[0]+w
    y =roi[1]+h
    
  # # RGBの各チャンネルのデータを一度に取得
    pixel = image[x, y,0]
    
    if pixel > median:
      image[x,y,:] = 255
    else :
      image[x,y,:] =0

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
      
    
    
  


 

