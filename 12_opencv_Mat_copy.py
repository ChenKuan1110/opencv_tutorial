import cv2
import numpy as np

'''
验证 opencv 中的 Mat 拷贝方式
'''
img = cv2.imread('./imgs/lenna.png')

# 浅拷贝
img2 = img
# 深拷贝
img3 = img.copy()

# 修改源图像中的局部内容
img[10:50, 10:50] = [0,0, 255]

cv2.imshow('origin', img)
cv2.imshow('shallow copy', img2)  # 验证结果为 浅拷贝， 拷贝图像也发生了内容变化
cv2.imshow('deep copy', img3)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

