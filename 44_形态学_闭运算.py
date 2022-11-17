import cv2
import numpy as np
from random import randint, seed

seed(100)

img = cv2.imread('./imgs/handwrite_binary_inv.png')

cv2.imshow('origin', img)

# kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
# # 实现闭合运算： 先腐蚀再膨胀
# dilate_res = cv2.dilate(img, kernel)
# dst = cv2.erode(dilate_res, kernel)
# cv2.imshow('dilate result', dst)

# 利用 opencv 提供的形态运算API进行闭运算
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
dst = cv2.morphologyEx(src=img,op=cv2.MORPH_CLOSE, kernel=kernel)
cv2.imshow('morphology close result', dst)

cv2.waitKey(0)


