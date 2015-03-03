# capture video

import cv2
import numpy as np

cap = cv2.VideoCapture('N:\project\Python_Files\a.mp4')


while (True):

    ret, frame = cap.read()
    print ret
    print frame
    #gray = cv2.cvtColor(frame, cv2.COLOR_RBG2GRAY)

    #cv2.imshow('Frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

    
