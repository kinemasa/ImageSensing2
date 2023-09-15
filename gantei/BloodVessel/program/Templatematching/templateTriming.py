"""
テンプレートマッチングを用いて動画から対象の画像群を切り出す

input :眼底画像群フォルダ
output :テンプレートマッチングを行ってトリミングを行った画像群
"""

import cv2
import numpy as np
import glob
import sys
import os


  
INPUT_DIR = '/Volumes/Extreme SSD/gantei1009/'
files = glob.glob(INPUT_DIR+'*')
OUTPUT_DIR= '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/result/triming/'
temp = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/template.png")
num = len(files)

##import picture
img_name = files[0]
img = cv2.imread(img_name)
img_copy=cv2.imread(img_name)

width = int(img.shape[1])
height = int(img.shape[0])



##import picture
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


