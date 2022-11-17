import cv2
import numpy as np

# 利用 opencv 中的 获取卷积核API 生成卷积核
k1 = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
print(k1)


# 调整 ksize
k2 = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(7,7))
print(k2)

# 调整 shape 为 椭圆形
k3 = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(7,7))
print(k3)

# 调整 shape 为 是十字形状
k4 = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(7,7))
print(k4)

img = cv2.imread('./imgs/handwrite_binary_inv.png')
cv2.imshow('origin', img)

# 对图像进行腐蚀
dst1 = cv2.erode(src=img, kernel=k1)
cv2.imshow('erode by k1', dst1)

dst2 = cv2.erode(src=img, kernel=k2)
cv2.imshow('erode by k2', dst2)

dst3 = cv2.erode(src=img, kernel=k3)
cv2.imshow('erode by k3', dst3)

dst4 = cv2.erode(src=img, kernel=k4)
cv2.imshow('erode by k4', dst4)

cv2.waitKey(0)

dst2 = cv2.erode(src=img, kernel=k2)
cv2.imshow('erode by k2', dst2)



