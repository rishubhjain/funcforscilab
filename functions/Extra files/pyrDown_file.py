import cv2.cv as cv
import cv2
import numpy as np

def pyrDown_path(path):

    image = cv2.imread(path)
    
    pyrdown_image = image.copy()
    
    for i in range(2):
        pyrdown_image = cv2.pyrDown(pyrdown_image)


    cv2.imshow("Source Image", image)
    cv2.imshow("PyrDown", pyrdown_image)
   


    
    cv2.waitKey(0)

    return

def pyrUp_path(path):

    image = cv2.imread(path)
    
    pyrdown_image = image.copy()
   
    for i in range(2):
        pyrdown_image = cv2.pyrDown(pyrdown_image)

    cv2.imshow("Source Image", image)
    cv2.imshow("PyrDown", pyrdown_image)
    cv2.waitKey(0)

    return


def pyrUp_image(img):

    image =img
    
    pyrdown_image = image.copy()
    
    for i in range(2):
        pyrdown_image = cv2.pyrDown(pyrdown_image)
    
    cv2.imshow("Source Image", image)
    cv2.imshow("PyrDown", pyrdown_image)
    cv2.waitKey(0)

    return

def pyrDown_image(img):

    image =img
    
    pyrdown_image = image.copy()
    
    for i in range(2):
        pyrdown_image = cv2.pyrDown(pyrdown_image)
    

    cv2.imshow("Source Image", image)
    cv2.imshow("PyrDown", pyrdown_image)
    
    cv2.waitKey(0)

    return
