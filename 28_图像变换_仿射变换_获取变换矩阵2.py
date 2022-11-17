import numpy as np

import cv2

img = cv2.imread('./imgs/cat.jpeg')
print(img.shape)
h, w, ch = img.shape

cv2.imshow('origin', img)

# 获取仿射变换矩阵的第二个api, 通过原图和目标图中三个点坐标确定
src = np.float32([(0,0), (100,100), (0,100)])
dst = np.float32([(10, 40), (80,80), (0, 200)])
M = cv2.getAffineTransform(src, dst)

img_tran = cv2.warpAffine(img, M=M, dsize=(w, h))
print(img_tran.shape)

cv2.imshow('translate', img_tran)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
