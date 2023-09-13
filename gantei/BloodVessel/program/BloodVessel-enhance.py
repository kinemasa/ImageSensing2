import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
import os
import sklearn
from skimage.exposure import rescale_intensity
from scipy import ndimage as nd
from skimage.morphology import label, remove_small_objects
from skimage.measure import regionprops, find_contours
from skimage.filters import threshold_otsu
from tqdm import tqdm

import function.extract_green_channel  as egc
import function.rotate_image as ri
import function.bloodEnhance as be
import function.imageSegmentation as ims
import function.vessel_skeleton_extraction as vse
import function.trimapFormation as tf



img = '/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/gantei/BloodVessel/src/gantei.tiff'


grChannel = egc.extract_green_channel(img)
rotategrChannel = ri.rotate_image(grChannel,10)
morphChannel= be.morph_reconstruct_filter(grChannel,10)
filtered_result, _, _ = be.isotropic_undec_wavelet_filter2D(grChannel)
background, Unknown, forground = ims.image_segmentation(grChannel)
vesselSkeleton = vse.vessel_skeleton_extraction(grChannel)
V1, U, _ = tf.trimap_formation(grChannel)


plt.imsave("grChannel.jpg",grChannel)
# plt.imsave("morph.jpg",morphChannel)
plt.imsave("wavelet.png",filtered_result)
plt.imsave("background.png",background)
plt.imsave("unknown.png",Unknown)
plt.imsave("forground.png",forground)
plt.imsave("vesselSkelton.png",vesselSkeleton)
plt.imsave("trimap.png",V1)