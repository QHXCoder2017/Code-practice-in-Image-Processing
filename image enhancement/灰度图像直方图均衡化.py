# 次数       概率           累计概率
# 1          P=0.2              0.2
# 2          P=0.3              0.5
# 3          P=0.1              0.6
# 一共256个灰度等级
# 比如100这个灰度等级，累计概率为0.5，255*0.5=new，制作一个100-new之间的映射，以后所有灰度等级为100的像素都用new这个新的像素来替代
# 替代完成后，整体的过程就叫做直方图的均衡化
import cv2
import numpy as np


img = cv2.imread('image0.jpg', 1)
imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('src', gray)
count = np.zeros(256, np.float32)
for i in range(0, height):  
    for j in range(0, width):
        pixel = gray[i, j]  # 获取每一个灰度等级的像素
        index = int(pixel)  
        count[index] = count[index] + 1  # 灰度等级计数+1
for i in range(0, 255):
    count[i] = count[i]/(height*width)  # 计算灰度等级出现的概率
# 计算累计概率
sum1 = float(0)  # sum1用来记录累计概率的和
for i in range(0, 255):  
    sum1 = sum1 + count[i]  # 累计概率
    count[i] = sum1  # 更新
# 计算映射表
map1 = np.zeros(256, np.uint16)  # 创建映射表
for i in range(0, 256):  
    map1[i] = np.uint16(count[i]*255)  # 每一个位置的累计概率*255再类型转换放入映射表中的每一个位置
# 映射
for i in range(0, height):  
    for j in range(0, width):
        pixel = gray[i, j]  
        gray[i, j] = map1[pixel]  # 用映射表进行替换
cv2.imshow('dst', gray)
cv2.waitKey(0)
