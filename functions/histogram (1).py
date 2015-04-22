import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram():

    img = cv2.imread('a.png',0)
    plt.hist(img.ravel(),256,[0,256])
    plt.show()
    cv2.waitKey(0)
    return
