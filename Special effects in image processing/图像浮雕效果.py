import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src1', img)
imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
dst = np.zeros((height, width, 1), np.uint8) 

for i in range(0, height):
    for j in range(0, width-1):  # 由于下面的j+1，这里width-1来防止越界
        grayP0 = int(gray[i, j])  # 当前像素，通过强制转换成int型同时获取灰度值
        grayP1 = int(gray[i, j+1])  # 与P0是相邻像素，行不变，列+1
        newP = grayP0 - grayP1 + 150  # 浮雕效果 +150是为了增加浮雕的灰度等级，相邻像素相减是为了突出边缘特征
        if newP > 255:
            newP = 255
        if newP < 0:
            newP = 0
        dst[i, j] = newP
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
