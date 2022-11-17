import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

cv2.imshow('origin', img)

# 使用 scharr 算子计算图像边缘 y 方向
d1 = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)
# x 方向
d2 = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)


dst = cv2.add(d1, d2)

cv2.imshow('d1', d1)
cv2.imshow('d2', d2)
cv2.imshow('dst', dst)



if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
