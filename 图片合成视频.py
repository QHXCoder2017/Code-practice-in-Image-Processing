import cv2


img = cv2.imread('image1.jpg')
imgInformation = img.shape
size = (imgInformation[1], imgInformation[0])
print(size)
videoWrite = cv2.VideoWriter('2.mp4', -1, 5, size)  # 写入对象，第二个参数选择一个可以使用的编码器，第三个参数帧率，第四个参数视频的大小

for i in range(1, 11):  
    fileName = 'image' + str(i) + '.jpg'
    img = cv2.imread(fileName) 
    videoWrite.write(img)  # 写入方法，参数为图片的数据
print('end')