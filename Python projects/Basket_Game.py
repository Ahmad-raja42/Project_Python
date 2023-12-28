import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np


cap = cv2.VideoCapture('Video/vid(4).mp4')

while True:
    success, img = cap.read()
    img  = img[0:9000, :]
    imgColor, mask = myColorFinder.update(img, hsvVals)
    imgContours, contours = cvzone.findContours(img, mask,minArea=500)
    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
        
    if posListX:
        A, B, C =np.polyfit(posListX, posListY, 2)
        
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    cv2.imshow("imgColor", imgContours)
    cv2.waitKey(100)        