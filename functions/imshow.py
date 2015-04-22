import numpy as np
import cv2

def imshow1(image):
    cv2.imshow('image',image)
    cv2.WaitKey(0)
    return 1
