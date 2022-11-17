import cv2
import numpy as np


img = np.zeros((480, 640, 3), np.uint8)

# 通道分离
b, g, r = cv2.split(img)
# print(b.shape, g.shape, r.shape)

b[50:100, 50:100] = 255
g[40:90, 40:90] = 255
r[60:110, 60:110] = 255

# 通道合并
img2 = cv2.merge((b, g, r))

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.imshow('img2', img2)


if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()