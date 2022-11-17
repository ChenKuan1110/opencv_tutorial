import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 直线绘制 坐标为(x, y)
cv2.line(img, pt1=(100,100), pt2=(200, 200), color=(0,0, 255), thickness=5)
cv2.line(img, pt1=(130,100), pt2=(230, 200), color=(0,0, 255), thickness=5, lineType=16)

# 绘制矩阵
cv2.rectangle(img, pt1=(100,100), pt2=(200, 200), color=(0,255, 0), thickness=1, lineType=cv2.LINE_4)

# 绘制园
cv2.circle(img, center=(320, 240), radius=50, color=(255,0,0),thickness=2, lineType=cv2.LINE_AA)

# 绘制椭圆
# 度数是按顺时针计算的 , angle 是从右侧开始的
cv2.ellipse(img, center=(320, 240), axes=(100, 50), angle=90, startAngle=0, endAngle=180,
            color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_4
            )

# 绘制多边形
pts = np.array([(320,240), (570,200), (480,320)], np.int32)  # 多边形的顶点
# print(pts)
cv2.polylines(img, pts=[pts], isClosed=True, color=(255, 255, 255))

# 填充多边形
cv2.fillPoly(img, pts=[pts], color=(0,255,255))


# 绘制文本
# cv2.tex()
cv2.putText(img, text="hello opencv", org=(100, 400), fontFace=cv2.FONT_ITALIC, fontScale=1, color=(0, 0, 255))


cv2.imshow('img', img)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()