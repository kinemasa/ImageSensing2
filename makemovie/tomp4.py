import glob
import cv2
import re
from constant import *

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

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