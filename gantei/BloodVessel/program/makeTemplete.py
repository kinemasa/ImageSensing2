# -*- coding: utf-8 -*-
import cv2
import numpy as np
import glob
import sys
import csv
import re
import os


def getVideoROI(img):
    roi = cv2.selectROI(img)
    cv2.destroyAllWindows()
    return roi

dir_name = '/Volumes/Extreme SSD/gantei1009/'

files = glob.glob(dir_name+'*')


img_name = files[0]
img = cv2.imread(img_name)
width = int(img.shape[1])
height = int(img.shape[0])

roi = getVideoROI(img)
print(roi)
width=50
height=50

#Crop Image
selectRoi_crop = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]

##ROI
cv2.rectangle(img,(roi[0],roi[1]),(roi[0]+roi[2],roi[1]+roi[3]),(0,0,200),3)


cv2.imwrite("template.png", selectRoi_crop)

cv2.imwrite("checkROI.png", img)


    