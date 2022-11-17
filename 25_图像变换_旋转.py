import cv2

img = cv2.imread('./imgs/img_1.png')

img_rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
img_rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('origin', img)
cv2.imshow('clockwise_90', img_rotate_90)
cv2.imshow('clockwise_180', img_rotate_180)
cv2.imshow('clockwise_270', img_rotate_270)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
