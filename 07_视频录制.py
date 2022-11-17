import cv2
import cv2 as cv

# fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # 指定视频编码器格式
fourcc = cv2.VideoWriter_fourcc('H', '2', '6', '4')  # 指定视频编码器格式
# 实例化 VideoWriter 参数为 ： 1.filename 2. fourcc 3. fps 4. frameSize 5. isColor
video_writer = cv.VideoWriter('save_video2.mp4', fourcc, 25, (1280, 720), True)

cap = cv.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('video', frame)
    # 写入当前帧到文件
    video_writer.write(frame)
    cmdVal = cv.waitKey(1) & 0xFF
    if cmdVal == ord('q'):
        break

cap.release()
# 释放 video_writer 资源 会将缓冲区中的数据（剩余未满部分）写入文件
video_writer.release()
cv.destroyAllWindows()