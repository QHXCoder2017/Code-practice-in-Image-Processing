import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
deep = imgInformation[2]  
newImgInformation = (height*2, width, deep)  
dst = np.zeros(newImgInformation, np.uint8) 

for i in range(0, height):  
    for j in range(0, width):
        dst[i, j] = img[i, j]  # 绘制原图片部分
        dst[height*2-i-1, j] = img[i, j]  # 绘制镜像图片部分
		
for i in range(0, width):  # 在镜像图片和原图片中间绘制分割线
    dst[height, i] = (0, 0, 255)  # 绘制红线
	
cv2.imshow('dst', dst)
cv2.waitKey(0)
