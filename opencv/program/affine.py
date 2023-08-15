import cv2
import numpy as np


def affine(img,moveX,moveY,angle,ratio):
    height,width = img.shape[:2]
    afn_mat = np.float32([[1,0,moveX],[0,1,moveY]])
    rot_mat = cv2.getRotationMatrix2D((width/2,height/2),angle,ratio)
    img_afn = cv2.warpAffine(img,afn_mat,(width,height))
    rot_afn = cv2.warpAffine(img_afn,rot_mat,(width,height))

    return rot_afn




if __name__ == "__main__":
    img = cv2.imread("opencv\src\ganteiBlood.png",0)
    affine_img = affine(img,moveX=0,moveY=0,angle=40,ratio=1)
    cv2.imshow("affine_img",affine_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()