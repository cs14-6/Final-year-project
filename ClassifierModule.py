__author__ = 'SPENCER LLOYD'

"""
Call different machine learning classifiers on data
"""
import cv2
import numpy as np


svm_params = dict( kernel_type = cv2.SVM_LINEAR, svm_type = cv2.SVM_C_SVC)
responses = np.float32(np.repeat(np.arange(10),250)[:,np.newaxis])

def calculateAccuracy(testTrueClasses, predictedClasses):
    "Function to calculate the prediction of the classifier"
    correct = np.count_nonzero(testTrueClasses == predictedClasses)
    accuracy = correct * 100.0/np.size(testTrueClasses)
    print correct
    return accuracy

def calcSensitivity(testTrueClasses, predictedClasses):
    correct = np.count_nonzero(testTrueClasses == predictedClasses)
    wrong = np.count_nonzero(testTrueClasses != predictedClasses)

    sensitivity = wrong * 100.0/np.size(testTrueClasses)
    print wrong
    return sensitivity

#check out 'http://docs.opencv.org/modules/ml/doc/ml.html' for a description of more

def naiveBayes(trainingData, trainingClasses, testData, testClasses):
    nbClassifier = cv2.NormalBayesClassifier()
    nbClassifier.train(trainingData, trainingClasses)
    ret, results = nbClassifier.predict(testData)
    print results
    return calculateAccuracy(testClasses, results), calcSensitivity(testClasses, results)

def kNN(trainingData, trainingClasses, testData, testClasses):
    kNNClassifier = cv2.KNearest()
    kNNClassifier.train(trainingData, trainingClasses)
    ret, results, neighbours, dist = kNNClassifier.find_nearest(testData, 3)
    print results
    return calculateAccuracy(testClasses, results), calcSensitivity(testClasses, results)

def SVM(trainingData, testData, testClasses):
    svm = cv2.SVM()
    #responses = np.float32(testData)
    #svm.train(np.array(trainingData), responses, params = svm_params)
    svm.train(trainingData, trainingClasses)
    result = svm.predict_all(testData)
    print result
    return calculateAccuracy(testClasses, result), calcSensitivity(testClasses, result)


dataName = 'dataimageData.npz'
# load data
data = np.load(dataName)
# can see what is in data by running data.files
trainingData = data['train']
trainingClasses = data['train_labels']
testData = data['test']
testClasses = data['test_labels']

print "Accuracy and Sensitivity from Naive Bayes:  {0} %".format(naiveBayes(trainingData, trainingClasses, testData, testClasses))
print "Accuracy and Sensitivity from K-Nearest Neighbour:  {0} %".format(kNN(trainingData, trainingClasses, testData, testClasses))
print "Accuracy and Sensitivity from SVM:  {0} %".format(SVM(trainingData, testData, testClasses))


