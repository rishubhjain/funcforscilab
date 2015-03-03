# Morphological operations

import cv2
import numpy as np

def erode_path(path,iterations):
    iterations=int(iterations)
    read_origional = cv2.imread(path,0)

    kernal = np.ones((5,5),np.uint8)

    erosion = cv2.erode( read_origional, kernal, iterations = 1)
    dst = np.hstack((read_origional,erosion))
    


    return dst

#grayscale image
def erode_image(image,iterations):
    iterations=int(iterations)
    read_origional = image

    kernal = np.ones((5,5),np.uint8)

    erosion = cv2.erode( read_origional, kernal, iterations)
    dst = np.hstack((read_origional,erosion))


    return dst


#grayscale image
def dilate(image,iterations):
    iterations=int(iterations)
    read_origional = image

    kernal = np.ones((5,5),np.uint8)

    dilation = cv2.dilate(read_origional, kernal, iterations)

    dst = np.hstack((read_origional, dilation))

    return dst
#grayscale image
def open(image):

    read_origional =image

    kernal = np.ones((5,5),np.uint8)

    opening = cv2.morphologyEx( read_origional, cv2.MORPH_OPEN, kernal )

    dst = np.hstack((read_origional, opening))

    return dst
#grayscale image
def close(image):

    read_origional = image

    kernal = np.ones((5,5),np.uint8)

    closing = cv2.morphologyEx( read_origional, cv2.MORPH_CLOSE, kernal )

    dst = np.hstack((read_origional, closing))


    return dst 
#grayscale image
def gradient(image):

    read_origional = image

    kernal = np.ones((5,5),np.uint8)

    gradient1 = cv2.morphologyEx( read_origional, cv2.MORPH_GRADIENT, kernal )

    dst = np.hstack((read_origional, gradient1))


    return dst
#grayscale image
def tophat(image):

    read_origional = image

    kernal = np.ones((9,9),np.uint8)

    tophat = cv2.morphologyEx( read_origional, cv2.MORPH_TOPHAT, kernal )

    dst = np.hstack((read_origional, tophat))


    return dst
#grayscale image
def blackhat(image):

    read_origional = image

    kernal = np.ones((9,9),np.uint8)

    blackhat = cv2.morphologyEx( read_origional, cv2.MORPH_BLACKHAT, kernal )

    dst = np.hstack((read_origional, blackhat))

    return dst
