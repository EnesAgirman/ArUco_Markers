import cv2 as cv
import numpy as np
from cv2 import aruco
import time

def findArucoMarkers(aImage, aDict):
    myImageGrayScaled = cv.cvtColor(aImage, cv.COLOR_BGR2GRAY)
    arucoParameters = aruco.DetectorParameters_create()
    boundaryBoxes, ID, rejectedImages = aruco.detectMarkers(myImageGrayScaled, aDict, parameters=arucoParameters)
    print(ID)

def playVideo():
    myVid = cv.VideoCapture(0)

    while 0xFF != ord(' '):
        captureSuccessfull, myFrame = myVid.read()
        cv.imshow("My Video", myFrame)
        findArucoMarkers(myFrame, aruco.Dictionary_get(aruco.DICT_4X4_50) )
        cv.waitKey(50)
        
        if cv.waitKey(1) & 0xFF == ord(' '):
            break    




playVideo()












print("\n\n\nleroleroleroleroleroleroleroleroleroleorlero\n\n\n")




