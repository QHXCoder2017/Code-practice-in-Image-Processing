import cv2


img = cv2.imread('naruto.jpg', 1)
cv2.imshow('src', img)

imgInformation = img.shape  # 获取图片的信息
height = imgInformation[0]  # 图片的高(矩阵的行)
width = imgInformation[1]  # 图片的宽(矩阵的列)

for m in range(100, 300):  # 遍历马赛克矩形区域内的像素点
    for n in range(100, 200):
        # pixel -> 10*10  选中元素，让这个元素替换掉10*10中的所有像素点并保持一致
        if m % 10 == 0 and n % 10 == 0:  # 在宽高每隔10个像素点的时候取1个像素
            for i in range(0, 10):  # 将小矩形框所有100个点全部填充
                for j in range(0, 10):
                    (b, g, r) = img[m, n]  # 读取b,g,r
                    img[i+m, j+n] = (b, g, r)  # 把读取的b,g,r放入，m和n分别对应马赛克矩形框的行和列
					
cv2.imshow('dst', img)
cv2.waitKey(0)
