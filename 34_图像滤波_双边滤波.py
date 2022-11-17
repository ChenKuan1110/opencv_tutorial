import cv2
import numpy as np

img = cv2.imread('./imgs/lenna.png')
# img = cv2.imread('./imgs/img_1.png')

cv2.imshow('origin', img)

# 使用双边滤波对图像进行处理
dst = cv2.bilateralFilter(src=img, d=5, sigmaColor=20, sigmaSpace=50)



cv2.imshow('dst', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
