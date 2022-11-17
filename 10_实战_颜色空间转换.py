import cv2 as cv
import numpy as np

WIN_NAME = 'color'
IMG_PATH = './imgs/lenna.png'
TRACKBAR_NAME = 'current_color'

cv.namedWindow(WIN_NAME)

img = cv.imread(IMG_PATH)

#
colors = [
    cv.COLOR_BGR2RGB,
    cv.COLOR_BGR2HSV,
    cv.COLOR_BGR2GRAY,
    cv.COLOR_BGR2HSV_FULL,
    cv.COLOR_BGR2YUV
]
cv.createTrackbar(TRACKBAR_NAME, WIN_NAME, 0, len(colors), lambda x: None)

while True:
    # 获取 trackbar 的值
    index = cv.getTrackbarPos(TRACKBAR_NAME, WIN_NAME)
    # 颜色空间转换API
    cvt_img = cv.cvtColor(img, colors[index])
    cv.imshow(WIN_NAME, cvt_img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()