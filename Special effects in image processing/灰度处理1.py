import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)
imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
mode = imgInformation[2]  # 当前每个像素由多少个颜色组成

# R=G=B == 灰度   (R+G+B)/3
dst = np.zeros((height, width, 3), np.uint8)  
for i in range(0, height):  
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 读取原图的像素点上的像素值BGR
        gray = (int(b) + int(g) + int(r))/3
        dst[i, j] = np.uint8(gray)  # 把灰度图像放到dst中
	
cv2.imshow('dst', dst)
cv2.waitKey(0)
