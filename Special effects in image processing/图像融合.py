import cv2
import numpy as np


img0 = cv2.imread('naruto.jpg', 1)
cv2.imshow('src1', img0)
img1 = cv2.imread('timg.jpg', 1)
cv2.imshow('src2', img1)

imgInformation = img0.shape  
height = imgInformation[0]  
width = imgInformation[1]  
roiH = int(height/2)  # 定义感兴趣范围
roiW = int(width/2)
img0ROI = img0[0:roiH, 0:roiW]  
img1ROI = img1[0:roiH, 0:roiW]  
dst = np.zeros((roiH, roiW, 3), np.uint8)  
dst = cv2.addWeighted(img0ROI, 0.4, img1ROI, 0.6, 0)  # dst = src1*a+src2*(1-a)

cv2.imshow('dst', dst)
cv2.waitKey(0)