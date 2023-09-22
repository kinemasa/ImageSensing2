import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/masayakinefuchi/labo/imagesensing2/ImageSensing2/clahe2.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

M = np.ones(image.shape, dtype="uint8") * 130

added_image = cv2.add(image, M)

subtracted_image = cv2.subtract(image, M)

plt.subplot(1, 3, 1)
plt.title('original')
plt.xticks([]), plt.yticks([])
plt.imshow(image)

plt.subplot(1, 3, 2)
plt.title('added_image')
plt.xticks([]), plt.yticks([])
plt.imshow(added_image)
plt.imsave("addimage.png",added_image)

plt.subplot(1, 3, 3)
plt.title('subtracted_image')
plt.xticks([]), plt.yticks([])
plt.imshow(subtracted_image)

plt.show()