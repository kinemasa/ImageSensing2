import cv2

img = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/clahe8.png")
# カラー→モノクロ変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 元画像の表示
cv2.imshow("src image", img)

# 大津の二値化
_, dst1 = cv2.threshold(
    img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("THRESH_OTSU", dst1)

# 適応的しきい値処理
dst2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 101, 10)
cv2.imwrite("adaptiveThreshold10110.png", dst2)

cv2.waitKey(0)