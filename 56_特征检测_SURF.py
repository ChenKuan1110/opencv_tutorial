import cv2
import cv2.xfeatures2d
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# SURF
surf = cv2.xfeatures2d.SURF_create()
# 检测和计算特征点与描述
kps, des = surf.detectAndCompute(image=gray, mask=None)

# 绘制特征点
cv2.drawKeypoints(gray, kps, img)


cv2.imshow('shi-tomasi', img)

cv2.waitKey()