#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np

def main():
    # 画像の取得
    im = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/vessel.png")

    # グレースケール変換
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # モノクロ変換
    bimg=cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2 )

   #bimg=cv2.bitwise_not(bimg) # モノクロ反転、しかしTHRESH_BINARY_INVで可能なことが判明したため備忘録として

    contours,hierarchy = cv2.findContours( bimg,  cv2.RETR_EXTERNAL | cv2.RETR_TREE  , cv2.CHAIN_APPROX_NONE)


    # ゴミ除去,面積50px以下を排除
    new_contours=[]
    FILL_COLOR=(0,0,0)
    AREA_MAX=300
    i=0

    
    for c in contours:
        s=abs(cv2.contourArea(c))
        if s <= AREA_MAX:
            new_contours.append(c)

    cv2.drawContours( im, new_contours, -1,FILL_COLOR,-1)

    cv2.imwrite("answer1.png",im)



if __name__ == '__main__':
    main()