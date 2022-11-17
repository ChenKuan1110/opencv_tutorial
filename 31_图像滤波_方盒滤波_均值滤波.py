import cv2
import numpy as np

img = cv2.imread('./imgs/beach-work1.jpg')

cv2.imshow('origin', img)

# 使用均值滤波对原图像进行滤波
dst = cv2.blur(src=img, ksize=(5,5))

# 使用 方盒滤波 API 进行滤波 同上面一样
dst = cv2.boxFilter(src=img, ddepth=-1, ksize=(5, 5), normalize=True)


cv2.imshow('dst', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
