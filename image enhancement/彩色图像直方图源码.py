import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
count_b = np.zeros(256, np.float32)
count_g = np.zeros(256, np.float32)
count_r = np.zeros(256, np.float32)

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]  
        index_b = int(b)  
        index_g = int(g)
        index_r = int(r)
        count_b[index_b] = count_b[index_b] + 1  # 统计b出现的次数
        count_g[index_g] = count_g[index_g] + 1  # g
        count_r[index_r] = count_r[index_r] + 1  # r
		
for i in range(0, 256):  # 遍历每个灰度等级
    count_b[i] = count_b[i] / (height * width)  # 把count_b中每一个灰度等级出现的次数进行归一化处理
    count_g[i] = count_g[i] / (height * width)
    count_r[i] = count_r[i] / (height * width)
	
x = np.linspace(0, 255, 256)  # 定义x轴的坐标
y1 = count_b  # 蓝色通道直方图的y轴坐标
plt.figure()
plt.bar(x, y1, 0.9, alpha=1, color='b')
y2 = count_g
plt.figure()
plt.bar(x, y2, 0.9, alpha=1, color='g')
y3 = count_r
plt.figure()
plt.bar(x, y3, 0.9, alpha=1, color='r')
plt.show()
cv2.waitKey(0)