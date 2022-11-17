import cv2 as cv

img = cv.imread('./imgs/lenna.png')
cv.imshow('show_img', img)

while True:
    if ord('q') == cv.waitKey(0) & 0xFF:
        break
cv.destroyAllWindows()