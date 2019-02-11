import cv2


cap = cv2.VideoCapture("1.mp4")  # 获取视频打开
isOpened = cap.isOpened()  # 判断是否打开
print(isOpened)

fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
print(fps, width, height)
i = 0  # i用来记录当前读取了多少张图片，初始值为0

while(isOpened):
    if i == 10:
        break
    else:
        i = i+1
    (flag, frame) = cap.read()  # 读取每一帧， flag表示是否读取成功，frame表示图片的内容
    fileName = 'image' + str(i) + '.jpg'  
    print(fileName)
    if flag == True:  # 表明读取图片成功
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])  # 第三个参数质量等级控制，100为质量最高
print('end')
# 该帧数为每秒29帧，人眼最低帧为15帧，当大于15帧时，视频看起来都是比较连续的