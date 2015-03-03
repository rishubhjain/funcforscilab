# This code has the functions related to adaptive threshold

import cv2
import numpy as np


#color image
def adaptive_thresh_mean(image,maxValue):
    read_original = image
    maxValue=int(maxValue)

    #Necessary to convert the image into grayscale
    gray = cv2.cvtColor(read_original,cv2.COLOR_RGB2GRAY) 

    th1 = cv2.adaptiveThreshold(gray,maxValue,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,2)
    dst = np.hstack((gray, th1))
    
    return dst

def adaptive_thresh_gaussian(image,maxValue):
    read_original = image
    maxValue=int(maxValue)
    #Necessary to convert the image into grayscale
    gray = cv2.cvtColor(read_original,cv2.COLOR_RGB2GRAY) 

    th1 = cv2.adaptiveThreshold(gray,maxValue,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    dst = np.hstack((gray, th1))
    
    return dst
