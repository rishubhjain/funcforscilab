# This function "getRotationMatrix2D" rotates the image by some degree which is given in parameter

import cv2
import numpy as np
from matplotlib import pyplot as plt

def getRotation(image,center1,angle,scale):

    read_original = image
    center_x=int(center1[0])
    center_y=int(center1[1])
    center=(center_x,center_y)
    rows,cols = read_original.shape
    scale=int(scale)
    T = cv2.getRotationMatrix2D((cols/2,rows/2),angle,scale)
    dst = cv2.warpAffine(read_original,T,(cols,rows))
    transformed = np.hstack((read_original,dst))

    return transformed

