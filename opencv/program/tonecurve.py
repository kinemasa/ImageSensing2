"""
画像の収縮と膨張を行う
入力：画像
出力：変換結果画像
"""

import cv2
import numpy as np
import binary as bi

def negaPosi(frame):
    return 255 - frame
  
def toneCurve1(frame, n = 1):
    look_up_table = np.zeros((256,1), dtype = 'uint8')
    for i in range(256):
        if i < 256 / n:
            look_up_table[i][0] = i * n
        else:
            look_up_table[i][0] = 255
    return cv2.LUT(frame, look_up_table)
  
def toneCurve2(frame, n = 1):
  look_up_table = np.zeros((256,1), dtype = 'uint8')
  for i in range(256):
      if i < 256 - 256 / n :
          look_up_table[i][0] = 0
      else:
          look_up_table[i][0] = i * n - 255 * (n - 1)
  return cv2.LUT(frame, look_up_table)

def sToneCurve(frame):
    look_up_table = np.zeros((256,1), dtype = 'uint8')
    for i in range(256):
        look_up_table[i][0] = 255 * (np.sin(np.pi * (i/255 - 1/2)) + 1) /2
    return cv2.LUT(frame, look_up_table)
  
def gammaCurve(frame, gamma = 0.5):
    look_up_table = np.zeros((256,1), dtype = 'uint8')
    for i in range(256):
        look_up_table[i][0] = pow(i / 255, 1 / gamma) * 255
    return cv2.LUT(frame, look_up_table)


if __name__ == "__main__":
    imgName  = "/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/median.jpg"
    img = cv2.imread(imgName)
    s = sToneCurve(img)
    cv2.imwrite("s.png",s)
    
 