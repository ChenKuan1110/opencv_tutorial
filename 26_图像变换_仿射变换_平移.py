import numpy as np

import cv2

img = cv2.imread('./imgs/cat.jpeg')
print(img.shape)
h, w, ch = img.shape

cv2.imshow('origin', img)

# 利用自定义平移矩阵的方式
M = np.float32([
    [1, 0, 100],
    [0, 1, 20]
])  # 转换为 float32 类型
print(M)

img_tran = cv2.warpAffine(img, M=M, dsize=(w, h))

cv2.imshow('translate', img_tran)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
