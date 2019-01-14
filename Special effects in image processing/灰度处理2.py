import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
mode = imgInformation[2]  # 当前每个像素由多少个颜色组成
dst = np.zeros((height, width, 3), np.uint8)  
for i in range(0, height):  
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 读取原图的像素点上的像素值BGR
        b = int(b)
	g = int(g)
        r = int(r)
        gray = r*0.299 + g*0.587 + b*0.114
        dst[i, j] = np.uint8(gray)
	
cv2.imshow('dst', dst)
cv2.waitKey(0)
