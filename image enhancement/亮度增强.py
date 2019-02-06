import cv2
import numpy as np


img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  # 获取图像的尺寸
height = imgInformation[0]
width = imgInformation[1]
dst = np.zeros((height, width, 3), np.uint8)

for i in range(0, height):  # 遍历图像
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 获取b,g,r
        bb = int(b) + 40  # 增加b的值
        gg = int(g) + 40
        rr = int(r) + 40
        if bb > 255:  
            bb = 255
        if gg > 255:
            gg = 255
        if rr > 255:
            rr = 255
        dst[i, j] = (bb, gg, rr)
		
cv2.imshow('dst', dst)
cv2.waitKey(0)