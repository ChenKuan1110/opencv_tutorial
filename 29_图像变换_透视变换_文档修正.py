import numpy as np
import cv2

WIN_NAME = 'origin'

points = []

cv2.namedWindow(WIN_NAME)

img = cv2.imread('./imgs/before.jpeg')
h, w, ch = img.shape

cv2.imshow(WIN_NAME, img)


# 增加对窗口的鼠标按下事件的捕获
def mouse_callback(event, x, y, flags, userData):
    if event == cv2.EVENT_LBUTTONDOWN:
        global points
        if len(points) == 4:
            transform(points)
        else:
            points.append([x, y])
            # 绘制点
            # cv2.circle(img,center=(x,y), radius=10, color=(0,0,255))
    else:
        pass


cv2.setMouseCallback(WIN_NAME, mouse_callback)


def transform(points):
    # 获取透视变换矩阵api
    # 通过找原图和目标图像上的四个定位点
    src = np.float32(points)
    dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    print(src)
    M = cv2.getPerspectiveTransform(src, dst)
    print(M)

    # 透视变换 api
    new = cv2.warpPerspective(img, M=M, dsize=(w, h))
    # 展示照片
    cv2.imshow('perspective', new)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
