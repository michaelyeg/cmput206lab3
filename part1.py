import cv2, math
from matplotlib import pyplot as plt
import numpy as np

class image:
    def __init__(self, filename):
        self.image = cv2.imread(filename, 0)
        self.filtered = []
        #self.height = 0
        #self.width = 0
        self.Gx = []
        self.Gy = []
        #self.getdimension()

    # Get image dimension (Height and Width)
    def getdimension(self):
        dimension = self.image.shape
        self.height = dimension[0]
        self.width = dimension[1]
        return

    def sobel(self):
        # Formula extracted from https://en.wikipedia.org/wiki/Sobel_operator

        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

        self.Gx = cv2.filter2D(self.image, -1, Kx)
        self.Gy = cv2.filter2D(self.image, -1, Ky)

        self.filtered = cv2.addWeighted(self.Gx, 0.5, self.Gy, 0.5, 0.0)
        return

    def display(self):
        plt.subplot(221), plt.imshow(self.image), plt.title('Before')
        plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(self.Gx), plt.title('Horizontal')
        plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(self.Gy), plt.title('Vertical')
        plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(self.filtered), plt.title('After')
        plt.xticks([]), plt.yticks([])
        plt.show()
        return


def main():
    img = image("ex2.jpg")
    img.sobel()
    img.display()
    return

if __name__ == "__main__":
    main()