import cv2
import matplotlib.pyplot as plt

import numpy as np
import extract_green_channel as egc
import bloodEnhance  as be
import imageSegmentation as ims


def vessel_skeleton_extraction(image):
    Iiuw, _, _  = be.isotropic_undec_wavelet_filter2D(image)
    per_px_inc = 0.3
    epsilon = 0.03
    mask = cv2.imread('C:\Users\kine0\labo\ImageSensing2\gantei\BloodVessel\\result\wavelet.png', 0)
    t = np.sort(np.ravel(Iiuw))
    thres = t[int(per_px_inc * len(t)) - 1] + epsilon
    a2 = 35 * 21 * max(Iiuw.shape) / min(Iiuw.shape)
    a1 = 2 * 21 * max(Iiuw.shape) / min(Iiuw.shape)
    bw = Iiuw < thres
    bw = bw.astype(np.uint8) * 255
    fil_bw = cv2.bitwise_and(bw,bw, mask = mask)
    m = np.ones_like(mask) * 255
    m1 = np.ones_like(mask) * 255
    contours, _ = cv2.findContours(fil_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area < a2):
            if(area < a1):
                cv2.drawContours(m1,[cnt],-1,0,-1)
            else:
                VRatio, extent, _ = ims.contourProps(cnt)
                if((VRatio >= 2.2)and(extent < 0.25)):
                    cv2.drawContours(m1,[cnt],-1,0,-1)
            cv2.drawContours(m,[cnt],-1,0,-1)
    T3 = cv2.bitwise_and(fil_bw, m, mask = mask) 
    vse = cv2.bitwise_and(fil_bw, m1, mask = mask)
    return vse


if __name__ =="__main__":
    img ="gantei/BloodVessel/src/gantei100.tiff"
    grChannel= egc.extract_green_channel(img)
    vessel =vessel_skeleton_extraction(grChannel)
    plt.imsave("vessel.png",vessel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()