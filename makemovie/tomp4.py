"""
画像群からmp4動画を作成する

input :眼底画像群フォルダ
output :テンプレートマッチングを行ってトリミングを行った画像群
"""

import glob
import cv2
import re


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


# 入力動画
# INPUT_VIDEO = 'd:\\gantei1009\\**.tiff'
INPUT_VIDEO = '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/result/triming/**.jpg'

# 出力動画 - ファイル名
OUTPUT_VIDEO = 'output7.mp4'
# 出力動画 - フレームレート
OUTPUT_FPS = 30

img_array = []
for filename in sorted(glob.glob(INPUT_VIDEO), key=natural_keys):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

video = cv2.VideoWriter(OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*'mp4v'), OUTPUT_FPS, size)

for i in range(len(img_array)):
    video.write(img_array[i])

video.release()