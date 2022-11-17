import cv2 as cv

cap = cv.VideoCapture('rtsp://admin:user12345@192.168.10.64:554/h264/ch1/sub/av/stream')

while True:
    isOK, frame = cap.read()
    # print(frame.shape)
    if not isOK:
        break
    cv.imshow('camera in office', frame)
    key = cv.waitKey(10) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite('111.png', frame)

cap.release()
cv.destroyAllWindows()