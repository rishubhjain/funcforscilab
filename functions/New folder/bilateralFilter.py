# bilateral filter... used for removing noise from the image and preserving the edges.

import cv2
import numpy as np

def bilateralFilter(img, d, sigmaColor, sigmaSpace):

    imgread = cv2.imread(img)

    d = int(d)
    sigmaColor = int(sigmaColor)
    sigmaSpace = int(sigmaSpace)

    cv2.bilateralFilter(imgread, d, sigmaColor, sigmaSpace)
    

    return imgread
