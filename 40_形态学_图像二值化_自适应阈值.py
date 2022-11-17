import cv2

# img = cv2.imread('./imgs/before.jpeg')
img = cv2.imread('./imgs/photo_with_shadow.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 使用全局二值化API 对图像进行二值化处理
ret, dst1 = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

# 使用自适应阈值二值化API 进行二值化处理
dst2 = cv2.adaptiveThreshold(
    src=gray,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY,
    blockSize=3,
    C=10
)

cv2.imshow('origin', img)
cv2.imshow('gray', gray)
cv2.imshow('binary', dst1)
cv2.imshow('adaptive', dst2)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()