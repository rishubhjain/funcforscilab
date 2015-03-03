# histogram2d in opencv

import cv2
import numpy as np

def histogram2d(img, channels):

    imgread = cv2.imread(img)
    channel1 = int(channels[0])
    channel2 = int(channels[1])

    channels = (channel1, channel2)

    hsv = cv2.cvtColor(imgread, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], channels, None, [180, 256], [0,180, 0, 256] )
    #cv2.imshow('a', hist)
    #cv2.waitKey(0)
    return hist
