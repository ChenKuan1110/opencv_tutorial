import cv2 as cv
import numpy as np


WIN_NAME = 'track_bar'

cv.namedWindow(WIN_NAME, cv.WINDOW_NORMAL)
cv.resizeWindow(WIN_NAME, 640, 480)

img = np.zeros((480, 640, 3), np.uint8)



def callback(any):
    pass


# 创建 trackbar
# cv.createTrackbar('my_first_track_bar', WIN_NAME, 18, 100, on_my_track_change)
cv.createTrackbar('R', WIN_NAME, 180, 255, callback)
cv.createTrackbar('G', WIN_NAME, 150, 255, callback)
cv.createTrackbar('B', WIN_NAME, 78, 255, callback)


if __name__ == '__main__':
    while True:
        # 获取 trackbar 的值
        r = cv.getTrackbarPos('R', WIN_NAME)
        g = cv.getTrackbarPos('G', WIN_NAME)
        b = cv.getTrackbarPos('B', WIN_NAME)

        # 设置图片的像素值
        img[:] = [b, g, r]

        cv.imshow(WIN_NAME, img)


        key = cv.waitKey(10)
        if key & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()