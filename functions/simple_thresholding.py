# In this file we will demonstrate the simple_thresholding functions.
#Note: The image shold be grayscale and 8 bit

import cv2
import numpy as np
#from matplotlib import pyplot as plt



def thresh_binary(image):
    read_original = image    
    ret,thresh1 = cv2.threshold(read_original, 127, 255, cv2.THRESH_BINARY)
    dst = np.hstack((read_original,thresh1))
    
    return dst

def thresh_binary_inv(image):
    read_original = image
    ret,thresh2 = cv2.threshold(read_original, 130, 255, cv2.THRESH_BINARY_INV)
    dst = np.hstack((read_original,thresh2))
    return dst

def thresh_trunc(image):
    read_original = image
    ret,thresh3 = cv2.threshold(read_original, 100, 255, cv2.THRESH_TRUNC)
    dst = np.hstack((read_original,thresh3))
    return dst

def  thresh_tozero(image):
    read_original = image
    ret,thresh4 = cv2.threshold(read_original, 135, 255, cv2.THRESH_TOZERO)
    dst = np.hstack((read_original,thresh4))
    return dst

def thresh_tozero_inv(image):
    read_original = image
    ret,thresh5 = cv2.threshold(read_original, 150, 255, cv2.THRESH_TOZERO_INV)
    dst = np.hstack((read_original,thresh5))
    return dst
