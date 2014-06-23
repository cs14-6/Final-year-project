__author__ = 'SPENCER LLOYD'


''' This class holds the functionality for image filtering and pre-processing '''

import cv2
from skimage import data, filter
import numpy as np
import os
import re

bins = 50 # length of data vector

#paths for image data access
dataFolderPath = 'data'

disease_train_path = 'training_data/deseased'
healthy_train_path = 'training_data/healthy'

disease_test_path = 'test data/deseased'
healthy_test_path = 'test data/healthy'


DELAY_CAPTION = 15000


def skimage_filter_technique(image_path):

    img2 = data.imread(image_path, True)
    tv_filter = filter.denoise_tv_chambolle(img2, weight=0.1)

    cv2.imshow('Gray Scale', tv_filter)
    cv2.waitKey(DELAY_CAPTION)

    return tv_filter



def getJpgImages(imgPath):
    images = next(os.walk(imgPath))[2]
    imgs = [os.path.join(imgPath, image) for image in images if re.search(r'\S+.jpg', image)]
    return imgs

#get images from the different folders
trainingDiseasedImages = getJpgImages(disease_train_path)
trainingHealthyImages = getJpgImages(healthy_train_path)

testDiseasedImages = getJpgImages(disease_test_path)
testHealthyImages = getJpgImages(healthy_test_path)



def calculateHistograms(images, bins):
    numOfImages = len(images)
    imageData = np.zeros((numOfImages, bins))
    for imageIndex in range(numOfImages):
        img = cv2.imread(images[imageIndex])
        img2 = skimage_filter_technique(images[imageIndex])
        hist = cv2.calcHist([img], [0], None, [bins], [0,256])
        imageData[imageIndex, :] = hist.transpose()
    return imageData


trainingDiseasedData = calculateHistograms(trainingDiseasedImages, bins).astype(np.float32)
trainingHealthyData = calculateHistograms(trainingHealthyImages, bins).astype(np.float32)
testDiseasedData = calculateHistograms(testDiseasedImages, bins).astype(np.float32)
testHealthyData = calculateHistograms(testHealthyImages, bins).astype(np.float32)


# define classes for the data, healthy - class 0, diseased - class - 1
trainingDiseasedClasses = np.ones((len(trainingDiseasedData),1)).astype(np.float32)
trainingHealthyClasses = np.zeros((len(trainingHealthyData),1)).astype(np.float32)
testDiseasedClasses = np.ones((len(testDiseasedData),1)).astype(np.float32)
testHealthyClasses = np.zeros((len(testHealthyData),1)).astype(np.float32)


# concatenate data
trainingData = np.vstack((trainingHealthyData, trainingDiseasedData))
trainingClasses = np.vstack((trainingHealthyClasses, trainingDiseasedClasses))

testData = np.vstack((testHealthyData, testDiseasedData))
testClasses = np.vstack((testHealthyClasses, testDiseasedClasses))

# save data to data folder
dataName = dataFolderPath + 'imageData.npz'
np.savez(dataName, train=trainingData, train_labels=trainingClasses, test = testData, test_labels=testClasses)

