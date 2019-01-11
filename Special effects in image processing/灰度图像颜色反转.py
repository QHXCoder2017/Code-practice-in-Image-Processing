import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
dst = np.zeros((height, width, 1), np.uint8)  # 1表示灰度图(单通道)

for i in range(0, height):
    for j in range(0, width):
        grayPixel = gray[i, j]  # 当前的每一个灰度值
        dst[i, j] = 255 - grayPixel  # 颜色反转放于新的数组
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
