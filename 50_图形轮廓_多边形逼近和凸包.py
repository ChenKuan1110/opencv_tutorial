import cv2
import numpy as np


def draw_shape(src, points):
    i = 0
    while i< len(points):
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x,y), (x1, y1), (0, 0, 255), 3)
        else:
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        i += 1


img = cv2.imread('./imgs/hand-removebg-preview.png')

# 转为单通道
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)

# 对图片进行二值化
ret, img_binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary', img_binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(image=img_binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print(f'检测出的轮廓数：{len(contours)}')
print(contours)
# 绘制轮廓
# contourIdx 绘制轮廓的索引， -1 表示绘制所有索引
cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2)

# 手型 检测结果中最符合的(此处为尝试出来的结果)
point = contours[8]
# 多边形逼近API
epsilon=10
approx = cv2.approxPolyDP(point, epsilon=epsilon, closed=True)
# print(approx.shape)
draw_shape(img, approx)
#
# # 多边形凸包API
hull = cv2.convexHull(point)
# print(hull)
draw_shape(img, hull)

cv2.imshow('origin', img)


cv2.waitKey()