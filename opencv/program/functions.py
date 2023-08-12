import cv2


def onTrackbar(position):
    global theshhold
    theshhold = position



"""
cv2.creataeTrackbar("track","img",trackValue=100,255,onTrackbar)

"""


def print_position(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
