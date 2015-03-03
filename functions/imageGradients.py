# Image Gradients
# 1. sobel operator
# 2. laplacian

import cv2
import numpy as np

def laplacian(img):

    imgread = cv2.imread(img)

    lap = cv2.Laplacian(imgread, cv2.CV_64F)

    return lap

def sobel(img, ddepth, xorder, yorder, ksize):

    imgread = cv2.imread(img)
    
    xorder = int(xorder)
    yorder = int(yorder)
    ksize = int(ksize)

    s = cv2.Sobel(imgread, cv2.CV_64F,xorder,yorder,ksize)

    return s
