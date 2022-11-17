import cv2

img = cv2.imread('../imgs/lenna.png')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', gray)

cv2.waitKey()
cv2.destroyAllWindows()