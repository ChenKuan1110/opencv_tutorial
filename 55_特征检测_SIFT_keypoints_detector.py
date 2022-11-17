import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# SIFT 操作
# 创建 sift 对象
sift = cv2.SIFT_create()
# # 检测角点
# kp = sift.detect(gray)

# 计算描述子
# kp, des = sift.compute(img, kp)

# 同时计算关键点和描述
kp, des = sift.detectAndCompute(image=gray, mask=None)

# # 绘制特征点
cv2.drawKeypoints(gray, keypoints=kp, outImage=img)


print(kp)
print('-'* 10)
print(des)

# 查看某一个描述点
print('&'* 50)
print(kp[0])
print(des[0])




cv2.imshow('shi-tomasi', img)

cv2.waitKey()