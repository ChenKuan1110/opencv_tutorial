import cv2

WIN_NAME = 'binary'

cv2.namedWindow(WIN_NAME, cv2.WINDOW_NORMAL)

img = cv2.imread('./imgs/lenna.png')
# print(img.shape)
# 转换为灰度图
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
# print(gray.shape)

# 使用二值化api 转换为
ret, dst = cv2.threshold(src=gray, thresh=180, maxval=2550, type=cv2.THRESH_BINARY_INV)
# print(ret,dst.shape)

cv2.imshow('origin', img)
cv2.imshow('gray', gray)

# 添加 trackbar
# 二值化只包含 THRESH_BINARY 和 THRESH_BINARY_INV 两种
type_arr = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
    cv2.THRESH_MASK,
    cv2.THRESH_OTSU,
    cv2.THRESH_TRIANGLE
]


def on_type_trackbar_change(pos):
    ret, dst = cv2.threshold(src=gray, thresh=180, maxval=2550, type=type_arr[pos])
    cv2.imshow(WIN_NAME, dst)


cv2.createTrackbar('type', WIN_NAME, 0, len(type_arr), on_type_trackbar_change)
cv2.imshow(WIN_NAME, dst)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()