import cv2.cv as cv
import cv2
import numpy as np

def gray2bgr():

    #imgloc = "C:\\Users\\Anjali\\Documents\\Python_Files\\a.png"

    read_origional = cv2.imread('a.png',0)
    cv2.imshow('Origional image',read_origional)
    
    dest=cv2.imread(imgloc,0)
    
    gray=cv2.cvtColor(read_origional,cv2.cv.CV_BGR2GRAY,dest)
    
    gray = cv2.cvtColor(gray,cv2.cv.CV_GRAY2BGR,dest)
    
    #show_converted = cv2.imshow('Converted Gray2bgr',gray)
    
    #cv2.waitKey(0)
    

    return gray
