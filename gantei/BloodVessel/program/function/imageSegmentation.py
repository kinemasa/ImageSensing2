import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

# from function import bloodEnhance  as be

# from function import extract_green_channel as egc
import bloodEnhance  as be
import extract_green_channel as egc


def contourProps(cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(cnt)
    aspect_ratio = float(w) / h
    extent = cv2.contourArea(cnt) / float(w * h)
    solidity = float(cv2.contourArea(cnt)) / hull_area
    return aspect_ratio, extent, solidity

def image_segmentation(image):
    Imr = be.morph_reconstruct_filter(image,10)
    # Imr = cv2.morphologyEx(Imr, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
    Imr = Imr / max(np.ravel(Imr))
    B = (Imr < 0.42)
    U = (Imr > 0.42) * (Imr < 0.75)
    V1 = (Imr > 0.75) * 255
    # img = cv2.cvtColor(V1.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(V1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
    V2 = np.zeros(V1.shape, dtype = np.uint8)
    a1 = 2 * 21* max(V1.shape) / min(V1.shape)
    for cnt in contours:
        if cv2.contourArea(cnt) > a1:
            VRatio, extent, _ = contourProps(cnt)
            if extent <= 0.35 and VRatio <= 2.2:
                cv2.fillPoly(V2, pts = [cnt], color = [255,255,255])
    V2 = V1 * V2
    return B, U, V2


if __name__ =="__main__":
    img ="gantei/BloodVessel/src/gantei100.tiff"
    grChannel= egc.extract_green_channel(img)
    morphChannel= be.morph_reconstruct_filter(grChannel,10)
    filtered_result, _, _ = be.isotropic_undec_wavelet_filter2D(grChannel)
    background, Unknown, forground = image_segmentation(grChannel)
    plt.imsave("background.png",background)
    plt.imsave("unknow.png",Unknown)
    plt.imsave("forward.png",forground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()