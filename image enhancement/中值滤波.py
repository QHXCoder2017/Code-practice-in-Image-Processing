import cv2
import numpy as np

# 比如3*3的模板，9个值进行排序，选择一个中间值替换掉原来的像素值

img = cv2.imread('image11.jpg', 1)

imgInformation = img.shape
height = imgInformation[0]
width = imgInformation[1]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('src', img)

dst = np.zeros((height, width, 3), np.uint8)
collect = np.zeros(9, np.uint8)  # 定义数组，装载模板中9个元素

for i in range(1, height-1):  # 遍历图像
    for j in range(1, width-1):
        k = 0  # 即将装取数字的下标
        for m in range(-1, 2):  # 3*3模板
            for n in range(-1, 2):
                gray = img[i+m, j+n]  # 获取当前灰度值
                collect[k] = gray  # 所有数据放入collect中
                k = k + 1
        # 排序
        for k in range(0, 9):
            p1 = collect[k]
            for t in range(k+1, 9):
                if p1 < collect[t]:
                    mid = collect[t]
                    collect[t] = p1
                    p1 = mid
        dst[i, j] = collect[4]  # 排序后，中间值位于collect数组的第5个位置上，角标对应4
		
cv2.imshow('dst', dst)
cv2.waitKey(0)