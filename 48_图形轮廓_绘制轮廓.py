import cv2
import numpy as np


img = cv2.imread('./imgs/contours1.png')


# 转为单通道
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# 对图片进行二值化
ret, img_binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img_binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(image=img_binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# 绘制轮廓
# contourIdx 绘制轮廓的索引， -1 表示绘制所有索引
res = cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=2)

cv2.imshow('draw contours result', res)

cv2.imshow('origin', img)

cv2.waitKey()