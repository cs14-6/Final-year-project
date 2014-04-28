__author__ = 'SPENCER LLOYD'


''' This class holds the functionality for image filtering and pre-processing '''

import cv2
from numpy import *
from matplotlib import pyplot as plt
from cv2 import SIFT


def read_and_clean_image(path):

    img = cv2.imread(path)

    DELAY_CAPTION = 15000

    for i in xrange(1, 10, 2):
        gaussian_blur = cv2.GaussianBlur(img, (i, i), 0)
        cv2.imshow('Blur', gaussian_blur)

    cv2.waitKey(DELAY_CAPTION)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    cv2.imshow('Gray Scale', thresh)
    cv2.waitKey(DELAY_CAPTION)


read_and_clean_image("skin141.png")

#sift = cv2.SIFT()
#kp = sift.detect(read_and_clean_image("O:/PROJECTS/SKIN/SKIN IMAGES/skin1.png"))
#kp, des = sift.compute(read_and_clean_image("O:/PROJECTS/SKIN/SKIN IMAGES/skin1.png"), kp)


