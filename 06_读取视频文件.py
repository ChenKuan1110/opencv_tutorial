import cv2 as cv

cap = cv.VideoCapture('./video/video.mp4')

# cv.VideoWriter()

while True:
    isOK, frame = cap.read()
    if not isOK:
        break
    cv.imshow('video', frame)
    key = cv.waitKey(40)
    if key & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
