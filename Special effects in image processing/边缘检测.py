import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src1', img)

imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]
  
# Sobel   第1步 算子模板  第2步 图片卷积  第3步 阈值判决
# 竖直方向上的模板[1 2 1       水平方向上的模板[1 0 -1
#                  0 0 0                        2 0 -2
#                 -1 -2 -1]                     1 0 -1]
# 卷积 算子方框中每一个元素对应相乘再求和
# [1 2 3 4]与[a b c d ]卷积 = a*1+b*2+c*3+d*4 = dst
# 竖直方向梯度a = 竖直方向上的算子与图片卷积，水平方向梯度b = 水平方向上的算子与图片卷积
# 幅值f = sqrt(a*a+b*b)，f>判决门限就是边缘，反之不是

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
dst = np.zeros((height, width), np.uint8)  
for i in range(0, height-2):  # 模板是3*3的，-2防止溢出
    for j in range(0, width-2):
        # y方向上的梯度，用灰度图与竖直方向上的模板矩阵卷积，一行一行的乘再相加
        gy = gray[i, j]*1 + gray[i, j+1]*2 + gray[i, j+2]*1 - gray[i+2, j] - gray[i+2, j+1]*2 - gray[i+2, j+2]*1
        # x方向上的梯度，用灰度图与水平方向上的模板矩阵卷积，一列一列的乘再相加
        gx = gray[i, j]*1 + gray[i+1, j]*2 + gray[i+2, j]*1 - gray[i, j+2]*1 - gray[i+1, j+2]*2 - gray[i+2, j+2]*1
        grad = np.emath.sqrt(gx*gx + gy*gy)
        if grad > 50:  
            dst[i, j] = 255  
        else:
            dst[i, j] = 0
			
cv2.imshow('dst', dst)
cv2.waitKey(0)
