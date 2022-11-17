import cv2
import numpy as np


img = cv2.imread('./imgs/contours1.png')
# cv2.imshow('origin', img)

# 转为单通道
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# print(gray.shape)
# cv2.imshow('gray', gray)

# 对图片进行二值化
ret, img_binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
# print(ret)
# print(img_binary.shape)
# print(img_binary)
cv2.imshow('binary', img_binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(image=img_binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(hierarchy)


cv2.waitKey()