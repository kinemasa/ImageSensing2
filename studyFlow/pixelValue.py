# -*- coding: utf-8 -*-
import cv2
import numpy as np
import glob
import sys
import csv
import re
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
  
def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi

dir_name ='/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/studyFlow/result/binaryTemplateImage/'
files = sorted(glob.glob(dir_name +'*'), key=natural_keys)

OUTPUT_DIR='/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/studyFlow/result/'

subject ='gantei30'
OUTPUT_FILE =OUTPUT_DIR +subject +'.csv'
num = len(files)

##import picture
img_name = files[0]

img = cv2.imread(img_name)
img_bit = cv2.bitwise_not(img)
width = int(img.shape[1])
height = int(img.shape[0])
cv2.imwrite("negamask.png",img_bit)
roi = getVideoROI(img_bit)
print(roi)

##脈波情報と時間を初期化する
pulsewave = np.zeros(int(num))
time = np.zeros(int(num))

i = 0
for f in files:
    
    img = cv2.imread(f)
    img = cv2.bitwise_not(img) 
    roi_width, roi_height = roi[2],roi[3]
    pixelNum = np.where(img<10,0,1)
    
    pulsewave[i] = np.sum(pixelNum[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2]),:])/3
   
    i += 1

    sys.stdout.flush()
    sys.stdout.write('\rProcessing... (%d/%d)' %(i,num))

i = 0

with open(OUTPUT_FILE, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for val in pulsewave:
        writer.writerow([val])
        i=i+1
