import numpy as np

import cv2

img = cv2.imread('./imgs/cat.jpeg')
print(img.shape)
h, w, ch = img.shape

cv2.imshow('origin', img)

# 利用API 获取一个二维的旋转仿射矩阵
# 旋转的角度为逆时针
M = cv2.getRotationMatrix2D(center=(w/2,h/2), angle=15, scale=0.3)
print(M)

# 缩放比例是原图的缩放比例，如果只设置 scale , 不会修改原图的尺寸
# 如果需要修改原图的尺寸，需要设置 dsize 的值
img_tran = cv2.warpAffine(img, M=M, dsize=(w, h))
print(img_tran.shape)

cv2.imshow('translate', img_tran)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
