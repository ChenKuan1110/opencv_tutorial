"""
基本功能： 可以通过鼠标进行基本图形的绘制
1. 当用户按下 L 键的时候，选择了画线， 移动鼠标即可画线
2. 当用户按下 R 键的时候，选择了画矩形， 移动鼠标即可画矩形
3. 当用户按下 C 键的时候，选择了画圆， 移动鼠标即可画圆
4. ...
"""
import cv2
import numpy as np

WIN_NAME = 'Drawing Board'
LINE_COLOR = (0, 255, 0)
THICKNESS = 2

current_shape = 0  # 当前绘制的形状 1-直线  2-矩阵 3-圆
start_pos = (0, 0)  # 绘制起始坐标点

img = np.zeros((1080, 1920, 3), np.uint8)
cv2.namedWindow(WIN_NAME)


def draw_shape(event, x, y, flags, userData):
    global start_pos, current_shape
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        start_pos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if current_shape == 1:  # line
            cv2.line(img, pt1=start_pos, pt2=(x,y), color=LINE_COLOR, thickness=THICKNESS)
        elif current_shape == 2:  # rectangle
            cv2.rectangle(img, pt1=start_pos, pt2=(x,y), color=LINE_COLOR, thickness=THICKNESS)
        elif current_shape == 3:  # circle
            r = int(((x - start_pos[0]) ** 2 + (y - start_pos[1])**2)**0.5)
            cv2.circle(img, center=start_pos, radius=r, thickness=THICKNESS, color=LINE_COLOR)
        else:
            print('no shape', current_shape)


cv2.setMouseCallback(WIN_NAME, draw_shape)

while True:
    cv2.imshow(WIN_NAME, img)
    key = cv2.waitKey(10) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l') or key == ord('L'):
        current_shape = 1
    elif key == ord('r') or key == ord('R'):
        current_shape = 2
    elif key == ord('c') or key == ord('C'):
        current_shape = 3
cv2.destroyAllWindows()