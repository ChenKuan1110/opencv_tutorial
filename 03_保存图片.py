import cv2 as cv

IMG_PATH = './imgs/lenna.png'

img = cv.imread(IMG_PATH)
cv.imshow('img', img)

while True:
    key = cv.waitKey() & 0xFF

    if key == ord('q'):
        cv.destroyAllWindows()
    elif key == ord('s'):
        cv.imwrite('saved.jpg', img)