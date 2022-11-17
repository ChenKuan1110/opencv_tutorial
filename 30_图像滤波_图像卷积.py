import cv2
import numpy as np

img = cv2.imread('./imgs/beach-work1.jpg')

cv2.imshow('origin', img)
kernel = np.ones((5,5), np.float32) / 25

# 进行卷积运算
dst = cv2.filter2D(img, ddepth=-1, kernel=kernel)  # ddpepth 目标图像深度 -1 表示和原图一样
cv2.imshow('dst', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
