__author__ = 'SPENCER LLOYD'

from skimage import data, filter
import cv2
from matplotlib import pyplot as plt

Delay = 15000

def skimage_filter_technique(image_path):

    img2 = data.imread(image_path, True)
    tv_filter = filter.denoise_tv_chambolle(img2, weight=0.1)

    cv2.imshow('Gray Scale', tv_filter)
    cv2.waitKey(Delay)

    return tv_filter


def show_histogram(image_path):
    image = cv2.imread(image_path)
    plt.hist(image.ravel(),256,[0,256]); plt.show()

show_histogram('train_healthy7.jpg')