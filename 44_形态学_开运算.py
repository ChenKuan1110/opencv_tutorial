import cv2
import numpy as np


img = cv2.imread('./imgs/handwrite_binary_inv.png')

cv2.imshow('origin', img)

kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
# 实现开运算： 先腐蚀再膨胀
# erode_res = cv2.erode(img, kernel)
# dst = cv2.dilate(erode_res, kernel)
# cv2.imshow('dilate result', dst)

# 利用 opencv 提供的开运算API
dst = cv2.morphologyEx(src=img,op=cv2.MORPH_OPEN, kernel=kernel)
cv2.imshow('morphology open result', dst)

cv2.waitKey(0)


