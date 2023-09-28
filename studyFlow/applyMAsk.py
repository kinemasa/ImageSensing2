"""
様々なフィルタを畳み込んで画像の特徴を強調する
"""

import cv2
import numpy as np
import glob
import os
import sys

def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi

def getTemplate(img):
  roi = getVideoROI(img)
  
  #Crop Image
  selectRoi_crop = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
  ##ROI
  cv2.rectangle(img,(roi[0],roi[1]),(roi[0]+roi[2],roi[1]+roi[3]),(0,0,200),3)
  
  cv2.imwrite("template.png", selectRoi_crop)
  cv2.imwrite("checkROI.png", img)
  return selectRoi_crop

def TemplateMatching(files,temp,OUTPUT_DIR):
  
  num = len(files)
  i = 0
  for f in files:
    basename=os.path.basename(f)
    root, ext = os.path.splitext(basename)
    
    img = cv2.imread(f)
    
    ##template matching
    temp_height,temp_width = temp.shape[:2]
    match = cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)#ZNCC
    min_value,max_value ,min_pt,max_pt = cv2.minMaxLoc(match)
    pt = max_pt

    selectRoi_crop = img[int(pt[1]):int(pt[1]+temp_height),int(pt[0]):int(pt[0]+temp_width)]
    output_file = OUTPUT_DIR + str(i) +".jpg"
    cv2.imwrite(output_file,selectRoi_crop)
    i += 1

    sys.stdout.flush()
    sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

  i = 0



def Median(img,filtersize):
  img_median =cv2.medianBlur(img,filtersize)
  return img_median

def sToneCurve(img):
    look_up_table = np.zeros((256,1), dtype = 'uint8')
    for i in range(256):
        look_up_table[i][0] = 255 * (np.sin(np.pi * (i/255 - 1/2)) + 1) /2
    return cv2.LUT(img, look_up_table)
  
def Chale(img,clipLimit,theGridSize):#default  3 ,(8,8)
  img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  clahe = cv2.createCLAHE(clipLimit,theGridSize)
  cl1 = clahe.apply(img_gray)
  return cl1

def adaptiveBinary(img,filtersize=101,substract_num=10):
  # 適応的しきい値処理
  dst2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, filtersize, substract_num)
  return dst2

def molphologyOpning(img):
  img = cv2.bitwise_not(img)
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
  dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
  dst = cv2.bitwise_not(dst)
  # cv2.imwrite("resultopen.png",dst)
  return dst

def mask(img,mask):
  mask = cv2.bitwise_not(mask)
  maskedImage = cv2.bitwise_and(img,mask)
  ##減算処理を行う
  M = np.ones(img.shape, dtype="uint8") * 50
  subtracted_image = cv2.subtract(maskedImage, M)
  # cv2.imwrite("mask.png",maskedImage)
  # cv2.imwrite("adjastMask.png",subtracted_image)
  return maskedImage
    
if __name__ == "__main__":
  
  INPUT_DIR = '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/studyFlow/result/templateImage/'
  files = glob.glob(INPUT_DIR+'*')
  basic_mask =cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/studyFlow/result/mask3/0.jpg",0)
  
  OUTPUT_MASK4= '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/studyFlow/result/mask4/'
  templatefiles = glob.glob(INPUT_DIR+'*')
  i =0
  for template in templatefiles:

    num = len(templatefiles)
    img = cv2.imread(template)
    img_median = Median(img,3)
    img_storn =sToneCurve(img_median)
    img_clahe =Chale(img_storn,clipLimit=3.0,theGridSize=(8,8))
    img_binary = adaptiveBinary(img_clahe)
    img_open  =molphologyOpning(img_binary)
    img_binary_median = Median(img_open,3)
    
    img_mask =mask(img_clahe,basic_mask)
    
    mask_dir =OUTPUT_MASK4+ str(i) +".jpg"
  
    cv2.imwrite(mask_dir,img_mask)
    
    i += 1
    sys.stdout.flush()
    sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

  i = 0
  
  
  
  


    
