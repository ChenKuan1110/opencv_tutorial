import cv2
import numpy as np

sky = cv2.imread('./imgs/blue-sky.jpeg')
print(sky.shape)
cat = cv2.imread('./imgs/cat.jpeg')
print(cat.shape)

img = cv2.addWeighted(sky, 0.2, cat, 0.8, 0)

cv2.imshow('sky', sky)
cv2.imshow('cat', cat)
cv2.imshow('result', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
