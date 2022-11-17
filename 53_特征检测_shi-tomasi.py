import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 利用 shi-tomasi 角点检测API
corners = cv2.goodFeaturesToTrack(
    image=gray,
    maxCorners=0,
    qualityLevel=0.01,
    minDistance=10
)

# 转换精度
corners = np.uint0(corners)
# print(corners)


for corner in corners:
    x, y = corner.ravel()
    # 绘制圆
    cv2.circle(img, center=(x,y), radius=3, color=(255,0,0),thickness=-1)


cv2.imshow('shi-tomasi', img)

cv2.waitKey()