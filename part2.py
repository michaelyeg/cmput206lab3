import cv2
import numpy as np
from matplotlib import pyplot as plt


def callback(x):
    MIN = cv2.getTrackbarPos('min', 'image')
    MAX = cv2.getTrackbarPos('max', 'image')
    edges = cv2.Canny(image, MIN, MAX)
    cv2.imshow('image', edges)
    return

image = cv2.imread("ex2.jpg", 0)
edges =[]
cv2.namedWindow('image')
# Create track bars
cv2.createTrackbar('min', 'image', 0, 255, callback)
cv2.createTrackbar('max', 'image', 0, 255, callback)

cv2.imshow('image',image)

while True:
    # Press ESC to quit
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()