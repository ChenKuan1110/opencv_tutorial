import cv2
import numpy as np
from random import randint, seed

seed(100)

img = cv2.imread('./imgs/handwrite_binary_inv.png')

cv2.imshow('origin', img)


# 利用 opencv 提供的形态运算API求梯度
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3, 3))
dst = cv2.morphologyEx(src=img,op=cv2.MORPH_GRADIENT, kernel=kernel)
cv2.imshow('morphology gradient  result', dst)

cv2.waitKey(0)


