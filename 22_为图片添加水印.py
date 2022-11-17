"""
为图片添加水印

步骤：
1. 导入一张需要添加水印的图片
2. 导入/创建 水印图片
3. 计算在什么地方添加，将添加的地方变为黑色
4. 利用 add 将两张图片叠加到一起
"""
import cv2
import numpy as np



# 读取需要添加水印的图片
img = cv2.imread('./imgs/beach-work1.jpg')

# 创建 logo 和 mask
logo = np.zeros((200,200,3), np.uint8)
mask = np.zeros((200,200), np.uint8)

# 绘制logo （模拟logo）
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [255, 0, 0]
# 对 mask 进行相同处理
mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

# 对 mask 按位取反
m = cv2.bitwise_not(mask)

# 选择添加水印的位置
roi = img[0:200, 0:200]

# 将选择的位置与 m 进行按位与操作
tmp = cv2.bitwise_and(roi, roi, mask=m)


# 将 logo 与 mask 进行按位异或
cv2.bitwise_xor(logo, logo, mask=mask)

# 将 tmp 与 logo 进行相加操作, 可以得到在logo 大小内与原图的效果
dst = cv2.add(logo, tmp)

# 将原图的区域替换位上面的 dst
img[0:200, 0:200] = dst

cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.imshow('roi', roi)
cv2.imshow('tmp', tmp)
cv2.imshow('dst', dst)
cv2.imshow('result', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

