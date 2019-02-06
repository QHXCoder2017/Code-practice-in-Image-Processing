import cv2
import numpy as np

# 定义6*6数据全为1的模板，用其乘以6*6矩阵中所有的图像数据，再除以36得到一个均值，把均值替换掉中心元素

img = cv2.imread('image11.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
dst = np.zeros((height, width, 3), np.uint8)

for i in range(3, height-3):
    for j in range(3, width-3):
        sum_b = int(0)  # 统计模板中的均值
        sum_g = int(0)
        sum_r = int(0)
        for m in range(-3, 3):
            for n in range(-3, 3):
                (b, g, r) = img[i+m, j+n]  # 读取图像中的每一个像素
                sum_b = sum_b + int(b)  # b本来是uint8类型，转换成int类型是防止相加的时候出现越界
                sum_g = sum_g + int(g)
                sum_r = sum_r + int(r)
        b = np.uint8(sum_b / 36)  # 求b的均值
        g = np.uint8(sum_g / 36)
        r = np.uint8(sum_r / 36)
        dst[i, j] = (b, g, r)  # 把新的b,g,r填充到目标图像中
		
cv2.imshow('dst', dst)
cv2.waitKey(0)