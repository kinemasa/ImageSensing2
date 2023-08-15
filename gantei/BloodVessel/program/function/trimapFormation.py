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
    mask = cv2.imread('c:/Users/kine0/labo/gantei/wavelet.png', 0)
    B = cv2.bitwise_and((B * 255).astype(np.uint8),(B * 255).astype(np.uint8), mask=mask)
    V = cv2.bitwise_or(V2, S, mask = mask)
    #V = cv2.bitwise_and(V, V, mask = ~B)
    U = (U * 127).astype(np.uint8)
    U = cv2.bitwise_and(U, U, mask = mask)
    return V, U, B

if __name__ =="__main__":
    img ="gantei/BloodVessel/src/gantei100.tiff"
    grChannel= egc.extract_green_channel(img)
    trimap = trimap_formation(grChannel)
    plt.imsave("trimap.png",trimap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()