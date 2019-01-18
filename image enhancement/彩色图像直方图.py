import cv2
import numpy as np


def ImageHist(image, type):
    color = (255, 255, 255)
    windowName = 'Gray'
    if type == 31:
        color = (255, 0, 0)
        windowName = 'B Hist'
    elif type == 32:
        color = (0, 255, 0)
        windowName = 'G Hist'
    elif type ==33:
        color = (0, 0, 255)
        windowName = 'R Hist'
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])  # 计算直方图，第一个参数为图片的数据，第二个参数为直方图的通道，灰度为0
# 第三个参数没模板，第四个参数为直方图有多少个柱，第五个参数为直方图各个像素值
    minV, maxV, minL, maxL = cv2.minMaxLoc(hist)  # 获取直方图最大值和最小值及其下标，为了归一化
    histImg = np.zeros([256, 256, 3], np.uint8)
	
    for h in range(256): 
        intenNormal = int(hist[h]*256/maxV)
        cv2.line(histImg, (h, 256), (h, 256-intenNormal), color)  # 绘制直方图
		
    cv2.imshow(windowName, histImg)
	
    return histImg

img = cv2.imread('image0.jpg', 1)
channels = cv2.split(img)  # 分解颜色通道

for i in range(0, 3):  
    ImageHist(channels[i], 31+i)  # 把每个颜色通道单独的值存进去，31表示是蓝色，通过+i能陆续得到绿色和红色
cv2.waitKey(0)