import cv2
import numpy as np

img = cv2.imread('./imgs/beach-work1.jpg')
print(img.shape)

img1 = np.ones(img.shape, np.uint8) * 50


result = cv2.subtract(img, img1)


cv2.imshow('origin', img)
cv2.imshow('add result', result)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()