__author__ = 'SPENCER LLOYD'

import numpy as np
import os
import re
import cv2
from skimage import data, filter



imgPath = 'newImg'

def skimage_filter_technique(image_path):
    img2 = data.imread(image_path, True)
    tv_filter = filter.denoise_tv_chambolle(img2, weight=0.1)
    cv2.imshow('Gray Scale', tv_filter)
    #cv2.waitKey(DELAY_CAPTION)
    return tv_filter


def getJpgImage(imgPath):
    images = next(os.walk(imgPath))[2]
    imgs = [os.path.join(imgPath, image) for image in images if re.search(r'\S+.jpg', image)]
    return imgs

getJpgImage()

def calculateHistograms(image, bins):
    numOfImages = len(image)
    imageData = np.zeros((numOfImages, bins))
    img = cv2.imread(image)
    img2 = skimage_filter_technique(image)
    hist = cv2.calcHist([img], [0], None, [bins], [0,256])
    imageData[image, :] = hist.transpose()
    return imageData

testHealthyClasses = np.zeros((len(imgPath),1)).astype(np.float32)