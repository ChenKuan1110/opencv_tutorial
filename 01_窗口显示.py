from random import random

import cv2
import numpy as np

WINDOW_NAME = 'new'

img = np.array([640, 480], dtype=np.uint8)
print(img[0:1,])
print(img.shape)

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 640, 480)
cv2.imshow(WINDOW_NAME, img)

while True:
    if ord('q') == cv2.waitKey(0):
        break
cv2.destroyAllWindows()