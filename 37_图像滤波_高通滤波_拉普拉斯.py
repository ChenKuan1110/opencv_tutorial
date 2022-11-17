import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

cv2.imshow('origin', img)

# 使用拉普拉斯(laplacian)算子计算边缘, 可以同时求边缘
dst = cv2.Laplacian(img, ddepth=cv2.CV_64F, ksize=3)

cv2.imshow('dst', dst)



if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
