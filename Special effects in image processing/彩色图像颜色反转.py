import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
dst = np.zeros((height, width, 3), np.uint8)  # 3表示彩色图

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 读取图像中b,g,r三种颜色
        dst[i, j] = (255-b, 255-g, 255-r)  # 彩色图像颜色反转放于dst矩阵中
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
