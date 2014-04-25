__author__ = 'SPENCER LLOYD'


''' This class holds the functionality for image filtering and pre-processing '''

import cv2
from numpy import *
from matplotlib import pyplot as plt
from PIL import Image
from cv2 import SIFT


img = cv2.imread("skin141.png", 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)

DELAY_BLUR = 5000
DELAY_CAPTION = 15000

for i in xrange(1, 10, 2):
    gaussian_blur = cv2.GaussianBlur(img, (i, i), 0)
    cv2.imshow('Blur', gaussian_blur)
    #cv2.waitKey(DELAY_BLUR)

cv2.waitKey(DELAY_CAPTION)
#cv2.destroyAllWindows()


im2 = cv2.imread("skin141.png")
gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow('Gray Scale', thresh)
cv2.waitKey(DELAY_CAPTION)

sift = cv2.SIFT()
kp = sift.detect(gray)
kp, des = sift.compute(gray, kp)


