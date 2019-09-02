import cv2
import numpy as np


img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  
height = imgInformation[0]
width = imgInformation[1]
count_b = np.zeros(256, np.float32)  # 用来存放蓝色通道里像素出现的概率
count_g = np.zeros(256, np.float32)
count_r = np.zeros(256, np.float32)

for i in range(0, height):  
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 获取b,g,r信息
        index_b = int(b)  
        index_g = int(g)
        index_r = int(r)
        count_b[index_b] = count_b[index_b] + 1  # 蓝色通道灰度等级计数+1
        count_g[index_g] = count_g[index_g] + 1
        count_r[index_r] = count_r[index_r] + 1
		
for i in range(0, 255):
    count_b[i] = count_b[i] / (height * width)  # 计算出蓝色通道灰度等级出现的概率
    count_g[i] = count_g[i] / (height * width)
    count_r[i] = count_r[i] / (height * width)
# 计算累计概率
sum_b = float(0)  # sum用来记录累计概率的和
sum_g = float(0)
sum_r = float(0)

for i in range(0, 255):  
    sum_b = sum_b + count_b[i]  # 计算蓝色通道的累计概率
    sum_g = sum_g + count_g[i]
    sum_r = sum_r + count_r[i]
    count_b[i] = sum_b  # 更新蓝色通道
    count_g[i] = sum_g
    count_r[i] = sum_r
# 计算映射表
map_b = np.zeros(256, np.uint16)  # 创建蓝色通道映射表
map_g = np.zeros(256, np.uint16)
map_r = np.zeros(256, np.uint16)

for i in range(0, 256):  
    map_b[i] = np.uint16(count_b[i] * 255)  # 每一个位置的累计概率*255再类型转换放入蓝色通道映射表中的每一个位置
    map_g[i] = np.uint16(count_g[i] * 255)
    map_r[i] = np.uint16(count_r[i] * 255)
# 映射
dst = np.zeros((height, width, 3), np.uint8)

for i in range(0, height):  
    for j in range(0, width):
        (b, g, r) = img[i, j]  # 获取当前b,g,r
        b = map_b[b]  # 将蓝色通道映射表中的值覆盖原来蓝色通道的值
        g = map_g[g]
        r = map_r[r]
        dst[i, j] = (b, g, r)  # 将更新过后的b,g,r的值赋给目标图像
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
