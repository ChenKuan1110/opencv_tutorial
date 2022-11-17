import cv2

img = cv2.imread('./imgs/lenna.png')
cv2.imshow('TEST', img)

while True:
    if ord('q') == cv2.waitKey(0):
        break

cv2.destroyAllWindows()