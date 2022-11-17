import cv2
import numpy as np

img = cv2.imread('./imgs/sudoku.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# 利用 harris 角点检测
dst = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
# Harris 角点的检测
img[dst>0.01* dst.max()] = [0,0, 255]



cv2.imshow('harris', img)

cv2.waitKey()