import numpy as np
import cv2

img = cv2.imread('./imgs/before.jpeg')
print(img.shape)
h, w, ch = img.shape

cv2.imshow('origin', img)

# 获取透视变换矩阵api
# 通过找原图和目标图像上的四个定位点
src = np.float32([[428, 331], [1352, 487], [30, 1609], [1208, 1780]])
dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
M = cv2.getPerspectiveTransform(src, dst)

# 透视变换 api
new = cv2.warpPerspective(img, M=M, dsize=(w, h))


cv2.imshow('perspective', new)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
