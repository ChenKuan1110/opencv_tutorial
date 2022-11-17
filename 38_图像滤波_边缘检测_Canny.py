import cv2
import numpy as np

# img = cv2.imread('./imgs/sudoku.jpeg')
img = cv2.imread('./imgs/img_1.png')

cv2.imshow('origin', img)

# 使用 Canny 计算边缘
dst = cv2.Canny(image=img, threshold1=40, threshold2=300)

cv2.imshow('dst by canny', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
