import cv2
import numpy as np

img = cv2.imread('./imgs/papper.png')

cv2.imshow('origin', img)

# 使用中值滤波对图像进行滤波
dst = cv2.medianBlur(img, ksize=5)

# 再滤波一次
dst1 = cv2.medianBlur(dst, ksize=5)


cv2.imshow('dst', dst)
cv2.imshow('dst1', dst1)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
