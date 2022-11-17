import cv2
import numpy as np


# 创建一张图片
img = np.zeros((200, 200), np.uint8)

# 调整部分区域
img[30:150, 30:150] = 255

# 创建一张新图片
img1 = np.zeros((200,200), np.uint8)
img1[60:180, 60:180] = 255



# 非运算
result_not = cv2.bitwise_not(img)

# 与运算
result_add = cv2.bitwise_and(img, img1)

# 或运算
result_or = cv2.bitwise_or(img, img1)

# 异或运算
result_xor = cv2.bitwise_xor(img, img1)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('bitwise_not', result_not)
cv2.imshow('bitwise_add', result_add)
cv2.imshow('bitwise_or', result_or)
cv2.imshow('bitwise_xor', result_xor)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
