# In image blurring(smmothning) will use four techniques:-
# 1. Averaging (blur(), boxFilter())

import cv2
import numpy as np



def myBlur(ksize):
    read_original = cv2.imread('a.png')
    #ksize = (int(a), int(b))
    anchor = (-1,-1) #default
    #borderType1 = BORDER_DEFAULT #default
    
    read_original = cv2.blur(read_original,  ksize, (-1,-1))

    #blurred = cv2.imshow('Blurred', dst)
    #cv2.waitKey(0)
    return read_original
    
    
