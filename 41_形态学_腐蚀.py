import cv2
import numpy as np


img = cv2.imread('./imgs/handwrite_binary_inv.png')
cv2.imshow('origin', img)

# 对图像进行腐蚀
kernel = np.ones((5,5))
dst = cv2.erode(img, kernel=kernel, iterations=1)

cv2.imshow('erode result', dst)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
