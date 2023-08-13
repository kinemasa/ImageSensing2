import cv2

"""
フィルタによる演算
"""
img = cv2.imread("opencv\src\ganteiBlood.png",0)
##平均化フィルタ
img_blur =cv2.blur(img,(3,3))
##ガウシアンフィルタ
img_gaussian =cv2.GaussianBlur(img,(9,9),2)
##メディアんフィルタ
img_median =cv2.medianBlur(img,5)
##メディアンフィルタ
img_bilateral =cv2.bilateralFilter(img,20,30,30)


"""
エッジ検出
"""
##Sobelxフィルター
sobelx_filter=cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3)
img_sobelx = cv2.convertScaleAbs(sobelx_filter)
##Sobelyフィルター
sobely_filter=cv2.Sobel(img,cv2.CV_32F,0,1,ksize=3)
img_sobely = cv2.convertScaleAbs(sobely_filter)

##ラプラシアンフィルタ
intensity =1
Laplacian_filter = cv2.Laplacian(img,cv2.CV_32F)*intensity
img_lap = cv2.convertScaleAbs(Laplacian_filter)

##ラプラシアン＋ガウシアン
Laplacian_Gaussian_filter = cv2.Laplacian(img_gaussian,cv2.CV_32F)
img_lapGau = cv2.convertScaleAbs(Laplacian_Gaussian_filter)

##Canny フィルタ
img_canny = cv2.Canny(img,10,110)

if __name__ == "__main__":
    img = cv2.imread("opencv\src\gantei100.tiff")
    Laplacian_Gaussian_filter = cv2.Laplacian(img_gaussian,cv2.CV_32F)
    img_lapGau = cv2.convertScaleAbs(Laplacian_Gaussian_filter)
    cv2.imshow("img",img_lapGau)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
