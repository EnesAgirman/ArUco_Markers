"""
Enes Agirman
July 5, 2023
This code generates aruco markers at the given file destination. It uses the dictionary
aruco.DICT_4X4_50 to get the aruco markers.

Sources:
1) https://pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/
2) https://python-academia.com/en/opencv-aruco/
3) https://docs.opencv.org/3.4/d9/d6a/group__aruco.html#ggac84398a9ed9dd01306592dd616c2c975ada8e830ff0024e839e93c01f5fed0c55

"""

import cv2 as cv
from cv2 import aruco
import numpy as np
import matplotlib.pyplot as plt
import os

# the file destination to save the aruco markers
aruco_markers_destination = r'aruco_markers'

# the number of aruco markers to be generated
ArucoNum = 20

# the size of the aruco markers
arucoSize = 500

# Specify the dictionary which we get the aruco markers from
myArucoDict = aruco.Dictionary_get(aruco.DICT_4X4_50 )

for i in range(ArucoNum):
    
    # draw the aruco markers as an image
    arucoImage = aruco.drawMarker(myArucoDict, i, arucoSize )

    # generate the filename for saving the aruco marker
    if i>9:
        ArucoImageFileName = "Aruco " + str(i) + ".jpg"
    else:
        ArucoImageFileName = "Aruco 0" + str(i) + ".jpg"
    
    # get the file path to save the aruco marker
    arucoImageFilePath = os.path.join(aruco_markers_destination, ArucoImageFileName)
    
    # save the aruco marker image as a file
    cv.imwrite(arucoImageFilePath, arucoImage)
    