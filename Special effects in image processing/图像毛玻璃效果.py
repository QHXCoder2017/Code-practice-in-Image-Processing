import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
dst = np.zeros((height, width, 3), np.uint8)  
mm = 8  # 随机选取元素的范围，水平方向和竖直方向都有可能

for m in range(0, height-mm):  # 遍历图像， -mm是为了防止越界
    for n in range(0, width-mm):
        index = int(np.random.random()*8)  # 产生0-8的随机数
        (b, g, r) = img[m+index, n+index]  # 给(m,n)大小的矩阵像素加上随机数产生毛玻璃效果
        dst[m, n] = (b, g, r)
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
