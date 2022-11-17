import cv2 as cv
import numpy as np

WIN_NAME = 'mouse control'

cv.namedWindow(WIN_NAME, cv.WINDOW_NORMAL)
cv.resizeWindow(WIN_NAME, (640, 480))


def mouse_callback(event, x, y, flags, userData):
    """
    :param event: 时间类型： 移动、按下、抬起
    :param x: x坐标
    :param y: y坐标
    :param flags: 左键 右键 中键 ctrl shift alt
    :param userData: 用户传递数据
    :return:
    """
    print(event, x, y, flags, userData)


# 设置鼠标回调函数
cv.setMouseCallback(WIN_NAME, mouse_callback, "123")

img = np.zeros((480, 640, 3), np.uint8)

while True:
    # 显示窗口
    cv.imshow(WIN_NAME, img)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()