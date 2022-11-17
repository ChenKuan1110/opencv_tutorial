import cv2 as cv

cap = cv.VideoCapture(1)

num = 1

while True:
    isOK, frame = cap.read()
    if not isOK:
        print('读入图像帧失败')
        break
    cv.imshow('视频内容', frame)
    if cv.waitKey(10) & 0xFF == ord('s'):
        cv.imwrite(f'./imgs/camera_img_{num}.png', frame)
        num += 1
    elif cv.waitKey(10) & 0xFF == ord('q'):
        break
    else:
        continue
cv.destroyAllWindows()
cap.release()  # 释放视频
