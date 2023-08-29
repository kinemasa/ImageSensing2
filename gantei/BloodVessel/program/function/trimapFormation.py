import cv2
import numpy as np
import matplotlib.pyplot as plt

import extract_green_channel as egc
import imageSegmentation as ims
import vessel_skeleton_extraction as vse

def trimap_formation(image):
    B, U, V2 = ims.image_segmentation(image)
    S = vse.vessel_skeleton_extraction(image)
    V2 = V2.astype(np.uint8)
    mask = cv2.imread('C:\\Users\\kine0\\labo\\ImageSensing2\\gantei\\BloodVessel\\src\\ganteiBlood.png', 0)
    plt.imsave("V2.png",V2)
    plt.imsave("S.png",S)
    B = cv2.bitwise_and((B * 255).astype(np.uint8),(B * 255).astype(np.uint8), mask=mask)
    V = cv2.bitwise_or(V2, S)
    #V = cv2.bitwise_and(V, V, mask = ~B)
    U = (U * 127).astype(np.uint8)
    U = cv2.bitwise_and(U, U, mask = mask)
    return V, U, B

if __name__ =="__main__":
    img ="C:\\Users\\kine0\\labo\\ImageSensing2\\gantei\\BloodVessel\\src\\ganteiBlood.png"
    grChannel= egc.extract_green_channel(img)
    trimap,_,_ = trimap_formation(grChannel)
    plt.imsave("trimap.png",trimap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()