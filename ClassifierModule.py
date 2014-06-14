__author__ = 'SPENCER LLOYD'

"""
Call different machine learning classifiers on data
"""
import cv2
import numpy as np

def calculateAccuracy(testTrueClasses, predictedClasses):
    "Function to calculate the prediction of the classifier"
    correct = np.count_nonzero(testTrueClasses == predictedClasses)
    accuracy = correct * 100.0/np.size(testTrueClasses)
    return accuracy

# define functions bfor different machine learning classifiers
# check out 'http://docs.opencv.org/modules/ml/doc/ml.html' for a description of more

def naiveBayes(trainingData, trainingClasses, testData, testClasses):
    nbClassifier = cv2.NormalBayesClassifier()
    nbClassifier.train(trainingData, trainingClasses)
    ret, results = nbClassifier.predict(testData)
    print results
    return calculateAccuracy(testClasses, results)

def kNN(trainingData, trainingClasses, testData, testClasses):
    kNNClassifier = cv2.KNearest()
    kNNClassifier.train(trainingData, trainingClasses)
    ret, results, neighbours, dist = kNNClassifier.find_nearest(testData, 3)
    print results
    return calculateAccuracy(testClasses, results)

def SVM(trainingData, trainingClasses, testData, testClasses):
    svm_params = dict(kernel_type = cv2.SVM_LINEAR, svm_type = cv2.SVM_C_SVC, c = 2.67, gamma = 5.383)
    SVMClassifier = cv2.SVM()
    SVMClassifier.train(trainingData, )





dataName = 'dataimageData.npz'
# load data
data = np.load(dataName)
# can see what is in data by running data.files
trainingData = data['train']
trainingClasses = data['train_labels']
testData = data['test']
testClasses = data['test_labels']

print "Accuracy from Naive Bayes:  {0} %".format(naiveBayes(trainingData, trainingClasses, testData, testClasses))
print "Accuracy from K-Nearest Neighbour:  {0} %".format(kNN(trainingData, trainingClasses, testData, testClasses))

