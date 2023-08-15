import cv2
import matplotlib.pyplot as plt
import math

##rotate_image
def rotate_image(image, angle):
    height, width = image.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_image = cv2.getRotationMatrix2D(image_center, angle, 1)

    radians = math.radians(angle)
    sin = math.sin(radians)
    cos = math.cos(radians)
    bound_w = int((height * abs(sin)) + (width * abs(cos)))
    bound_h = int((height * abs(cos)) + (width * abs(sin)))

    rotation_image[0, 2] += ((bound_w / 2) - image_center[0])
    rotation_image[1, 2] += ((bound_h / 2) - image_center[1])

    rotated_image = cv2.warpAffine(image, rotation_image, (bound_w, bound_h))
    return rotated_image 
