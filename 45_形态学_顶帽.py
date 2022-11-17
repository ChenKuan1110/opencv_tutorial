import cv2
import numpy as np

# img = np.zeros((300, 300, 3), np.uint8)
#
# img[20:280, 20:200] = [255, 255, 255]
# img[40: 60, 260:280] = [255, 255, 255]
# img[140: 160, 260:280] = [255, 255, 255]
# img[240: 260, 260:280] = [255, 255, 255]
# cv2.imwrite('./imgs/tophat.png', img)

img = cv2.imread('./imgs/tophat.png')
cv2.imshow('origin', img)

# 利用 opencv 提供的形态运算API求顶帽效果
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(21,21))
dst = cv2.morphologyEx(src=img,op=cv2.MORPH_TOPHAT, kernel=kernel)
cv2.imshow('morphology tophat  result', dst)

cv2.waitKey(0)


