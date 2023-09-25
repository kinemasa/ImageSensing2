import cv2

# 画像を読み込む
# 画像1
img1 = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/adaptiveThreshold.png")
# 画像2
img2 = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/adaptiveThreshold.png")

# A-KAZE検出器の生成
akaze = cv2.AKAZE_create()

# 画像を読込、特徴量を計算
# kp=keypoints(特徴点抽出), des=descriptors(特徴点描画)
# detectAndCompute() => (kp:特徴点の一覧, des:各特徴点の特徴量記述子)  のタプルになります。
kp1, des1 = akaze.detectAndCompute(img1, None)
kp2, des2 = akaze.detectAndCompute(img2, None)

# 特徴量のマッチングを実行
bf = cv2.BFMatcher() # 総当たりマッチング(Brute-Force Matcher)生成
# 特徴量ベクトル同士をBrute-ForceとKNN(kth-nearest neighbor)でマッチング
matches = bf.knnMatch(des1, des2, k=2)

# データをマッチング精度の高いもののみ抽出
ratio = 0.8
good = []
for m, n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])
        
# 対応する特徴点同士を描画
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# 画像表示
cv2.imshow('img', img3)

# キー押下で終了
cv2.waitKey(0)
cv2.destroyAllWindows()