import cv2

img = cv2.imread('./imgs/img_1.png')
cv2.imshow('origin', img)
flip_img_x = cv2.flip(img, flipCode=0)  # flipCode = 0 沿 x 轴进行翻转
flip_img_y = cv2.flip(img, flipCode=1)  # flipCode = 正数， y
flip_img_both = cv2.flip(img, flipCode=-1) # flipCode = 负数 两个轴
flip_img_y2 = cv2.flip(img, flipCode=10)  # flipCode = 正数， y


cv2.imshow('flip x', flip_img_x)
cv2.imshow('flip y', flip_img_y)
cv2.imshow('flip y2', flip_img_y2)
cv2.imshow('flip both', flip_img_both)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
