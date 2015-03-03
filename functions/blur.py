#Averaging

import cv2
import numpy as np

def blur(img,kSize):
    
    imgread = cv2.imread(img)

    kSize1 = int(kSize[0])
    kSize2 = int(kSize[1])

    kSize = (kSize1, kSize2)

    b = cv2.blur(imgread, kSize)

    return b
