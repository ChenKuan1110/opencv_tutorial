import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

cv2.imshow('origin', img)

# 使用 sobel 算子计算 y 方向的边缘
d1 = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=2, dy=0, ksize=5)
# 计算 x 方向的边缘
d2 = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=2, ksize=5)

# 将计算出来的两个方向的结果进行相加
# dst = d1 + d2  # 直接利用加法
dst = cv2.add(d1, d2)

cv2.imshow('d1', d1)
cv2.imshow('d2', d2)
cv2.imshow('dst', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
