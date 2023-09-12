"""
  テンプレートマッチングを行うプログラム
"""

import cv2

if __name__ =="__main__":
  #input image
   img = cv2.imread('/Volumes/Extreme SSD/gantei1009/2023-08-17 20-04-44.800_gantei1009_2_1.tiff')
   temp = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/src/gantei.tiff")
   
   
   height,width = temp.shape[:2]
   
   
   ##template matching
   match = cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)#ZNCC
   min_value,max_value ,min_pt,max_pt = cv2.minMaxLoc(match)
   pt = max_pt
   ##output result
   cv2.rectangle(img,(pt[0],pt[1]),(pt[0]+width,pt[1]+height),(0,0,200),3)
   cv2.imwrite("result"+ ".jpg",img)