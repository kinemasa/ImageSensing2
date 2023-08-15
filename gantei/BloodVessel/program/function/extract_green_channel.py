import cv2
import numpy as np

def extract_green_channel(file):
    img = cv2.imread(file)
    gr = np.zeros_like(img)
    gr = img[:,:,1]
    return gr


if __name__ =="__main__":
    img ="gantei/BloodVessel/src/gantei100.tiff"
    greenImg = extract_green_channel(img)
    cv2.imshow("greenImg",greenImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
