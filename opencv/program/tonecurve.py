import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image, display

def plot_grayscale_conversion(src, dst):
    fig = plt.figure(figsize=(10, 6))
    ax1 = plt.subplot2grid((3, 2), (0, 0), rowspan=2)
    ax2 = plt.subplot2grid((3, 2), (0, 1), rowspan=2)
    ax3 = plt.subplot2grid((3, 2), (2, 0))
    ax4 = plt.subplot2grid((3, 2), (2, 1))
    # 入力画像を描画する。
    ax1.set_title("Input")
    ax1.imshow(src, cmap="gray", vmin=0, vmax=255)
    ax1.set_axis_off()
    # 出力画像を描画する。
    ax2.set_title("Output")
    ax2.imshow(dst, cmap="gray", vmin=0, vmax=255)
    ax2.set_axis_off()
    # 入力画像のヒストグラムを描画する。
    ax3.hist(src.ravel(), bins=256, range=(0, 255), color="k")
    ax3.grid()
    ax3.set_xticks([0, 255])
    ax3.set_yticks([])
    # 出力画像のヒストグラムを描画する。
    ax4.hist(dst.ravel(), bins=256, range=(0, 255), color="k")
    ax4.set_xticks([0, 255])
    ax4.set_yticks([])
    ax4.grid()
    plt.show()


# 画像を読み込む。
img = cv2.imread("C:\\Users\\kine0\\labo\\ImageSensing2\\opencv\\src\\gantei101.tiff",0)

# ネガポジ反転
def negaposi(img):
    x = np.arrange(256)
    y = 255 -x

    dst = cv2.LUT(img, y)
    plot_grayscale_conversion(img, dst)

# 2値化
def binary(img):
    x = np.arange(256)
    y = np.where(x <= 95 , 0, 255)
    

    dst = cv2.LUT(img, y)
    plot_grayscale_conversion(img, dst)


def postarization(img,n):# 画素値を何段階で表現するか
    x = np.arange(256)
    bins = np.linspace(0, 255, n + 1)
    y = np.array([bins[i - 1] for i in np.digitize(x, bins)]).astype(int)
    dst = cv2.LUT(img, y)
    plot_grayscale_conversion(img, dst)


def enhanceContrust(img):
    t = 155
    x = np.arange(256)
    y = np.clip(255 / t * x, 0, 255)

    dst = cv2.LUT(img, y)
    plot_grayscale_conversion(img, dst)





if __name__ == "__main__":
    img = cv2.imread("opencv\src\wavelet.png",0)
    binary(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
