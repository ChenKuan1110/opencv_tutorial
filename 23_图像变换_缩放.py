import cv2


# 大图缩小
# img = cv2.imread('./imgs/beach-work.jpg')
# cv2.imshow('origin', img)
# # 指定缩放插值算法，不指定默认为 INTER_NEAREST（邻近插值）
# resize_img = cv2.resize(img, dsize=None, fx=0.3, fy=0.3, interpolation=cv2.INTER_NEAREST)
# cv2.imshow('resize', resize_img)


img = cv2.imread('./imgs/cat.jpeg')
cv2.imshow('origin', img)
resize_img = cv2.resize(img, dsize=None, fx=10, fy=10, interpolation=cv2.INTER_AREA)
cv2.imshow('resize', resize_img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
