"""
画像の領域の面積によって指定より小さい範囲を黒色に塗りつぶす

input :眼底画像 ,取り除く最大面積
output :領域削除画像
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def removeArea(img,AREA_MAX):

   
    # グレースケール変換
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # モノクロ変換
    bimg=cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2 )
    contours,hierarchy = cv2.findContours( bimg,  cv2.RETR_EXTERNAL | cv2.RETR_TREE  , cv2.CHAIN_APPROX_NONE)


    # ゴミ除去,面積50px以下を排除
    new_contours=[]
    FILL_COLOR=(0,0,0)
    
    i=0

    
    for c in contours:
        s=abs(cv2.contourArea(c))
        if s <= AREA_MAX:
            new_contours.append(c)

    cv2.drawContours(img, new_contours, -1,FILL_COLOR,-1)

    cv2.imwrite("answer1.png",img)



if __name__ == '__main__':
    # 画像の取得
    img = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/vessel.png")
    removeArea(img,300)
    