import cv2
import numpy as np


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src1', img)
imgInformation = img.shape  
height = imgInformation[0]  
width = imgInformation[1]
  
# 第1步转化成灰度；第2步将图片分割为若干个小方块，统计小方块中每一个像素的灰度值；
# 第3步将0-255划分为几个等级，并把第二步处理的结果映射到这几个灰度等级内,256个灰度等级分为4个段，第一段0-63，第二段64-127；
# 第四步找到每个方块中灰度等级最多的所有像素，并求取这些像素的均值；
# 第五步用统计出来的平均值替换原来的像素值

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
dst = np.zeros((height, width, 3), np.uint8)
  
for i in range(4, height-4):
    for j in range(4, width-4):
        array1 = np.zeros(8, np.uint8)  # 定义一个数组来装载8个灰度等级里的像素个数
        for m in range(-4, 4):  # 定义8*8的小方块
            for n in range(-4, 4):
                p1 = int(gray[i+m, j+n]/32)  # 除以32，来确定灰度等级在8个灰度等级段里的哪一个，p1= 0 到 7
                array1[p1] = array1[p1] + 1  # 当前像素值累加
        currentMax = array1[0]  # 假设array1[0]中的像素值最多
        l = 0  # 记录灰度段
        for k in range(0, 8):  
            if currentMax < array1[k]: 
                currentMax = array1[k]  
                l = k  # 更新灰度段
        for m in range(-4, 4):  # 遍历小方块
            for n in range(-4, 4):
                if gray[i+m, j+n] >= (l*32) and gray[i+m, j+n] <= ((l+1)*32):  # 如果像素值位于某一个灰度段内，取出来小方块中最后一个满足条件的灰度值
                    (b, g, r) = img[i+m, j+n]
        dst[i, j] = (b, g, r)
		
cv2.imshow('dst', dst)
cv2.waitKey(0)
