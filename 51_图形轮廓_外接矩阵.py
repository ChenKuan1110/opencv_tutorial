import cv2
import numpy as np


def draw_shape(src, points):
    """
    绘制检测形状的方法
    :param src: 原图
    :param points: 检测结果的点
    :return: None
    """
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


img = cv2.imread('./imgs/hello.png')

# 转为单通道
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)

# 对图片进行二值化
ret, img_binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary', img_binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(image=img_binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print(f'检测出的轮廓数：{len(contours)}')
# print(contours)


# 最小外接矩形
rect = cv2.minAreaRect(points=contours[1])
box = cv2.boxPoints(rect) # 找旋转矩形的四个顶点
box = np.int0(box)
# 绘制轮廓
cv2.drawContours(img, [box], 0, (0,0,255), 2)


# 最大外接矩阵
rect1 = cv2.boundingRect(contours[1])
print(rect1)
# 绘制
x, y, w, h = rect1
cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)


cv2.imshow('result', img)

cv2.waitKey()