__author__ = 'SPENCER LLOYD'


''' This class holds the functionality for image filtering and pre-processing '''

import cv2
from numpy import *
from matplotlib import pyplot as plt
from skimage import data, filter
from skimage.filter import threshold_adaptive




DELAY_CAPTION = 15000
def read_and_clean_image(path):

    img = cv2.imread(path)

    cv2.imshow('Normal', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    cv2.imshow('Gray Scale', thresh)
    cv2.waitKey(DELAY_CAPTION)


def skimage_filter_technique():

    img2 = data.imread('img_res/inf_skin141.png', True)
    tv_filter = filter.denoise_tv_chambolle(img2, weight=0.1)

    cv2.imshow('Gray Scale', tv_filter)
    cv2.waitKey(DELAY_CAPTION)

    return tv_filter


def threshold_skin_image(skin_image):

    block_size = 40
    adaptive_threshold = threshold_adaptive(skin_image, block_size, offset=10)

    plt.imshow(adaptive_threshold)
    plt.show()


threshold_skin_image(skimage_filter_technique())