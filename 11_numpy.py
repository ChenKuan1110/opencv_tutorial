import cv2
import numpy as np

########################## 创建数组

# 1. np.array()
# a = np.array([1, 2, 3])
# b = np.array([[1,2,3], [4, 5, 6]])
# print(a)
# print(b)

# 全0/1 数组
# c = np.zeros([8, 8, 3], np.uint8)
# c1 = np.ones([8, 8, 3], np.uint8)
# print(c)
# print(c1)
# img = np.zeros((480, 640, 3), np.uint8)  # (480, 640, 3) 可以理解为（行的个数，列的个数，通道数/层数）
# print(img.shape)


# 全值矩阵 full
# d = np.full([8, 8], 10, np.uint8)
# print(d)

# 单元矩阵
# e = np.identity(5)  # 5 行 5 列的单元矩阵
# print(e)

# 非正方形的单位矩阵
# f = np.eye(5, 6, 1)  # 5 行 6列 的矩阵，第一行从第二个元素开始沿"对角线"的值为1，其余值为0
# print(f)


############## 检索与赋值
# img = np.zeros((640, 480,3), np.uint8)
# # cv2.imshow('img', img)
#
# # 检索
# print(img[5:7, 8])
#
# # 赋值
# count = 0
# while count < 100:
#     img[0:count, 200] = [0, 255, 0]
#     count += 1
# cv2.imshow('img add a line', img)
#
#
# if cv2.waitKey(0) & 0xff == ord('q'):
#     cv2.destroyAllWindows()


############### ROI (Region Of Image)
img = np.zeros((640, 480,3), np.uint8)
cv2.imshow('origin', img)

roi = img[200:400, 100: 300]  # 通过 [y1:y2, x1:x2] 提取图像中的部分区域
# roi[:, :] = [255, 0, 0]  # 通过 [:, :] 或 [:] 对图像整个区域进行重新赋值
roi[:] = [255, 255, 255]
roi[:, 10] = [0,0,0]  # x = 10 的所有列
roi[10,:] = [0, 255, 0]  # y = 10 的所有行
roi[10:100, 30: 180] = [0, 0, 255]
cv2.imshow('sub img（roi）', roi)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
