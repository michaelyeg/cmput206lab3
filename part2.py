import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


class image:
    def __init__(self, filename):
        self.image = cv2.imread(filename, 0)
        self.edges = []

    def custom_canny(self):
        cv2.namedWindow('Custom Canny')

        # Create track bars
        cv2.createTrackbar('min', 'image', 0, 255, nothing)
        cv2.createTrackbar('max', 'image', 0, 255, nothing)

        while True:
            # Press ESC to quit
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

            MIN = cv2.getTrackbarPos('min', 'image')
            MAX = cv2.getTrackbarPos('max', 'image')

            self.edges = cv2.Canny(self.image, MIN, MAX)
            cv2.imshow('image', self.edges)

        cv2.destroyAllWindows()
        return


def main():
    img = image("ex2.jpg")
    img.custom_canny()

if __name__ == "__main__":
    main()
