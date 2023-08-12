import cv2
import numpy as np


"""
入力　img
     gammaValue : γ値
"""
def gamma(img,gammaValue):
    
    img = cv2.imread("opencv\src\ganteiBlood.png")
    gamma_cvt = np.zeros((256,1), dtype=np.unit8)

    for i in range(256):
        gamma_cvt[i][0] = 255 *(float(i)/255)**(1.0/gammaValue)

    img_ganma = cv2.LUT(img,gamma_cvt)

    return img_ganma


if __name__ == "__main__":
    img = cv2.imread("opencv\src\ganteiBlood.png")
    cv2.imwrite("opencv\\result\\img.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()