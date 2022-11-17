import cv2
import numpy as np

img = cv2.imread('./imgs/lenna.png')

# Mat 的一些属性
print(img.shape)  # 高度 宽度 通道数
# 图片占用空间 高度 x 宽度 x 通道数
print(img.size)
# 图像中每个元素的位深
print(img.dtype)