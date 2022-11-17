import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# SIFT 操作
# 1. 创建 sift 对象
sift = cv2.xfeatures2d.SIFT_create()
# 2. 检测角点
kp = sift.detect(gray)
# 3. 绘制特征点
cv2.drawKeypoints(gray, keypoints=kp, outImage=img)



cv2.imshow('shi-tomasi', img)

cv2.waitKey()