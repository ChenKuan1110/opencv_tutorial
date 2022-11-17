import cv2
import numpy as np

img = cv2.imread('./imgs/beach-work1.jpg')
print(img.shape)

# 图的加法运算就是矩阵的加法运算 ，因此两张图必须是相等的（高度，宽度，位深）
img1 = np.ones(img.shape, np.uint8) * 50
# print(img.shape)
# print(img1[10:12])

result = cv2.add(img, img1)


cv2.imshow('origin', img)
cv2.imshow('add result', result)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()