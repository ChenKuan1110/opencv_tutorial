import cv2
import numpy as np


img = cv2.imread('./imgs/tophat.png')
cv2.imshow('origin', img)

# 利用 opencv 提供的形态运算API求黑帽效果
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(21,21))
dst = cv2.morphologyEx(src=img,op=cv2.MORPH_BLACKHAT, kernel=kernel)
cv2.imshow('morphology blackhot  result', dst)

cv2.waitKey(0)


