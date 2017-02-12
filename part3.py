import cv2, math
from matplotlib import pyplot as plt


class image:
    def __init__(self, filename):
        self.image = cv2.imread(filename, 0)
        self.filtered = []
        self.height = 0
        self.width = 0
        # Use the switch to identify if self.gaussianfilter() has been called before
        self.switch = 0
        self.getdimension()
        # Standard Deviation of the image
        self.stdDev = self.getstdDev()

    def getstdDev(self):
        # http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#cv2.meanStdDev
        return cv2.meanStdDev(self.image)[1][0][0]

    # Get image dimension (Height and Width)
    def getdimension(self):
        dimension = self.image.shape
        self.height = dimension[0]
        self.width = dimension[1]
        return

    # Apply gaussianfilter
    def gaussianfilter(self):
        if self.switch == 0:
            self.filtered = cv2.GaussianBlur(self.image, (5, 5), 0)
            self.switch = 1
        else:
            self.filtered = cv2.GaussianBlur(self.filtered, (5, 5), 0)
        return


class mask:
    def __init__(self, image):
        self.height = image.height * 2
        self.width = image.width * 2
        self.center = (image.width, image.height)
        self.weight = [[0 for x in range(self.width)]for y in range(self.height)]
        self.generate(image)

    def generate(self, image):
        x0 = image.height
        y0 = image.width
        for x in range(self.height):
            for y in range(self.width):
                self.weight[x][y] = math.exp(-((x-x0)**2+(y-y0)**2)/(image.stdDev**2))
        return

def blur(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print (x, y)

global img
img = image("ex1.jpg")
img.gaussianfilter()
cv2.namedWindow('image')
cv2.setMouseCallback('image', blur)
MASK = mask(img)
print MASK.weight

while True:
    cv2.imshow('image', img.image)
    # Press ESC to quit
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()