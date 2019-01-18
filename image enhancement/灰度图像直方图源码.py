import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = np.zeros(256, np.float32)

for i in range(0, height):  
    for j in range(0, width):
        pixel = gray[i, j]  
        index = int(pixel)  
        count[index] = count[index] + 1  # 灰度等级计数+1
		
for i in range(0, 255):
    count[i] = count[i]/(height*width)  # 计算灰度等级出现的概率
	
x = np.linspace(0, 255, 256)  # X轴0-255的数据，总共256个
y = count  # Y轴
plt.bar(x, y, 0.9, alpha=1, color='b')  # 第1、2个参数为横纵坐标，第3个参数为每一个条占整个的百分比
plt.show()
cv2.waitKey(0)