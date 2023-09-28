# -*- coding: utf-8 -*-
import cv2
import numpy as np
import glob
import sys
import csv
import re
import os
import _funcSkinSeparation2 as ss
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
  
def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi

dir_name ='/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/'
files = sorted(glob.glob(dir_name +'img_binary.png'), key=natural_keys)

OUTPUT_DIR='/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/skinSeparation/_skinColorSeparation/result/'

subject ='gantei30'
OUTPUT_FILE =OUTPUT_DIR +subject +'.csv'
num = len(files)
print(files)
##import picture
img_name = files[0]
print(img_name)
img = cv2.imread(img_name)


width = int(img.shape[1])
height = int(img.shape[0])

roi = getVideoROI(img)
print(roi)
##select position ROI_size
# width=50
# height=50
# x1 = 924
# y1 = 450

#Crop Image(ROI)
selectRoi_crop = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
#Crop   Image(selected_ROI)
# fixedRoi_crop = img[int(y1):int(y1+height),int(x1):int(x1+width)]

cv2.imwrite("selectedRoi.png", selectRoi_crop)
# cv2.imwrite("fixedRoi.png", fixedRoi_crop)
# cv2.imwrite("output.png",img_copy)




##脈波情報と時間を初期化する
pulsewave = np.zeros(int(num))
time = np.zeros(int(num))

i = 0
for f in files:
    
    img = cv2.imread(f)
    
    ##平均画素値を色素成分関数に入力して得られたヘモグロビン画像の値で取得
    
    ##ROI
    img_roi = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    roi_width, roi_height = roi[2],roi[3]
    img_roi = np
    pulsewave[i] = np.sum(img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2]),:])
    
    #fixedSIze
    #pulsewave[i] = np.mean(ss.skinSeparation(img[int(roi[1]):int(roi[1]+height),int(roi[0]):int(roi[0]+width),:],"Hemoglobin"))
    
    #fixedSize , fixed SIze
    #pulsewave[i] = np.mean(ss.skinSeparation(img[int(y1):int(y1+height),int(x1):int(x1+width),:],"Hemoglobin"))
    i += 1

    sys.stdout.flush()
    sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

i = 0

with open(OUTPUT_FILE, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for val in pulsewave:
        writer.writerow([val])
        i=i+1
