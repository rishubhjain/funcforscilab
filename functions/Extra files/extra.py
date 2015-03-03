import cv2
import numpy as np

def matrix(img1,cent,radius):
    thickness = 1
    lineType = 8
    a=int(cent[0])
    b=int(cent[1])
    
    radius=int(radius)
    center=(a,b)
    img=cv2.imread('a.png')
    color=(0,0,255)
    cv2.circle(img, center, radius,color, thickness,lineType)
    cv2.imshow("rishubh",img)
    cv2.waitKey(0)
    
    return

def mat(img1):
    
    return

def myCircle(img):
    thickness = 1
    lineType = 8
    #linetype default 8
    #thickness default 1
    #color default (0,0,255)
    #a=int(cent[0])
    #b=int(cent[1])
    

    #center=(a,b)
    center=(2,5)
    radius=5

    color=(0,0,255)

    cv2.circle(img,
               center,
               radius,
               color,
               thickness,
               lineType)
    
    return 
