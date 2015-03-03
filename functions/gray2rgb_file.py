import cv2.cv as cv
import cv2
import numpy as np

def gray2rgb():

    #imgloc = "C:\\Users\\Anjali\\Documents\\Python_Files\\a.png"

    read_origional = cv2.imread('a.png',0)
    cv2.imshow('Origional image',read_origional)
    
    dest=cv2.imread(imgloc,0)
    
    gray=cv2.cvtColor(read_origional,cv2.cv.CV_RGB2GRAY,dest)
    
    gray1 = cv2.cvtColor(gray,cv2.cv.CV_GRAY2RGB,dest)
    
    cv2.imshow('Converted Gray2rgb',gray1)
    
    cv2.waitKey(0)
    

    return 
