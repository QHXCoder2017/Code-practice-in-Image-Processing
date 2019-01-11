import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
dst = np.zeros(img.shape, np.uint8) 

for i in range(0, height):  
    for j in range(0, width-100):  # 向右移
        dst[i, j+100] = img[i, j]
		
cv2.imshow('image', dst)
cv2.waitKey(0)
