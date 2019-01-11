import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
dstHeight = int(height / 2)
dstWidth = int(width / 2)
dstImg = np.zeros((dstHeight, dstWidth, 3), np.uint8)

for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i * (height*1.0 / dstHeight))
        jNew = int(j * (width*1.0 / dstWidth))
        dstImg[i, j] = img[iNew, jNew]
        
cv2.imshow('dst', dstImg)
cv2.waitKey(0)
