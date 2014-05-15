__author__ = 'SPENCER LLOYD'


''' This class holds the functionality for image filtering and pre-processing '''

import cv2
from matplotlib import pyplot as plt
from skimage import data, filter
from skimage.filter import threshold_adaptive
import numpy as np
import csv



DELAY_CAPTION = 15000


def skimage_filter_technique():

    img2 = data.imread('img_res/inf_skin141.png', True)
    tv_filter = filter.denoise_tv_chambolle(img2, weight=0.1)

    cv2.imshow('Gray Scale', tv_filter)
    cv2.waitKey(DELAY_CAPTION)

    return tv_filter


def array_generator(skin_image):
    image_array = np.asarray(skin_image)
    return image_array


def threshold_skin_image(skin_image):

    block_size = 40
    adaptive_threshold = threshold_adaptive(skin_image, block_size, offset=10)

    plt.imshow(adaptive_threshold)
    plt.show()

    return adaptive_threshold


def feed_Training_Data(training_data, path):

    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in training_data:
            writer.writerow(line)

    #training_data = array_generator(skimage_filter_technique())
    #path = "training_data.csv"





def flatten_data(nested_list):
    for i in nested_list:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten_data(i):
                yield j
        else:
            yield i



new_list = flatten_data(array_generator(skimage_filter_technique()))

feed_Training_Data(new_list, "training_data.csv")