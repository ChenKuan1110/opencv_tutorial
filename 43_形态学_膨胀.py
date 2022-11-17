import cv2
import numpy as np


img = cv2.imread('./imgs/handwrite_binary_inv.png')

cv2.imshow('origin', img)
h, w, d = img.shape

# for w in range(w):
#     for h in range(h):
#         pass



# 膨胀操作
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(7,7))
print(kernel)
dst = cv2.dilate(src=img, kernel=kernel, iterations=1)
cv2.imshow('dilate result', dst)

cv2.waitKey(0)


