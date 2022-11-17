import cv2
import numpy as np

img = cv2.imread('./imgs/lenna.png')

cv2.imshow('origin', img)

# 使用高斯滤波对原图像进行滤波
dst = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=1)


cv2.imshow('dst', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
