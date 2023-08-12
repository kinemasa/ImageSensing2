import cv2
import matplotlib.pyplot as plt


import functions as f

img = cv2.imread("opencv\src\ganteiBlood.png",0)




window_title="trackbar"

def onTrackbar(val):
     if img is not None:
        # 二値化
        ret, img_th = cv2.threshold(img, val, 255, cv2.THRESH_BINARY)
        # 画像の表示
        cv2.imshow(window_title, img_th)

##トラックバーの値を参照して二値化する
def binary_threshold(img):
    cv2.namedWindow(window_title)
    threshold =10
    cv2.createTrackbar("track",window_title,threshold,255,onTrackbar)
    # トラックバーの値を取得
    track_value = cv2.getTrackbarPos("track", window_title)
    # 最初の１回目の処理を取得した値で実行
    onTrackbar(track_value)
    cv2.waitKey()

##大津の二値化とあだによる二値化
def binary_otsu(img):
    cv2.namedWindow(window_title)
    
    ret2,img_otsu =cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    img_ada=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
    
    return img_ada







# img_ada=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)




if __name__ == "__main__":
    img = cv2.imread("opencv\src\ganteiBlood.png",0)
    #binary_threshold(img)
    img_binary = binary_otsu(img)
    cv2.imshow("img_binary",img_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
