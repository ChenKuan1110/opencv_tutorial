import cv2

min_w = 80  # 车辆轮廓矩形的最小宽度
min_h = 80

cars = []  # 存放车辆中心点的坐标

count = 0  # 车辆统计数量

line_height = 480  # 检测线在视频画面中的高度
offset = 6  # 检测线偏移量


def center(x, y, w, h):
    """
    获取中心点
    :param x: 矩形 x 坐标
    :param y: 矩形 y 坐标
    :param w: 矩形宽度
    :param h: 矩形高度
    :return: 中心点坐标 (x, y)
    """
    return int(x) + int(w/2) , int(y) + int(h /2)


# 创建背景
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

# 形态学 kernel
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))

# 1. 加载视频
cap = cv2.VideoCapture('video1.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 2. 去噪
    # 灰度处理
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 去噪（高斯）5
    blur = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=5)
    # 去背景
    mask = bgsubmog.apply(frame)
    # cv2.imshow('mask', mask)

    # 3. 形态学处理
    # 腐蚀 去掉图中的小斑块
    erode = cv2.erode(mask, kernel=kernel, iterations=1)
    # cv2.imshow('erode', erode)
    # 膨胀 还原放大
    dilate = cv2.dilate(erode, kernel=kernel, iterations=3)
    # cv2.imshow('dilate', dilate)

    # 闭操作， 去掉物体内部的小块
    close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('close operate', close)

    # 4. 轮廓查找
    contours, heir = cv2.findContours(close, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    # 绘制检测线
    cv2.line(frame, (10, line_height), ( frame.shape[1] - 10, line_height), color=(0, 255, 0), thickness=3)

    for (i, c) in enumerate(contours):
        # 获取外接矩形宽高位置
        x, y, w, h = cv2.boundingRect(c)

        # 对车辆的宽高进行判断，验证是否是有效的车辆
        isValid = (w >= min_w) and (h >= min_h)
        if not isValid:
            continue
        # 绘制检测车辆的矩形
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

        # 选取符合条件的车辆的中心点坐标，如果其越过了规定的线，判定为车辆
        car_center_point = center(x, y, w, h)
        cars.append(car_center_point)
        cv2.circle(frame, car_center_point, 5, (0,0,255), -1)

        print(f'==> {len(cars)}')
        # 判定车辆中心点与 画线位置的坐标之间的关系，来统计车辆数量
        # 弊端： 多检、漏检
        for (x, y) in cars:
            if line_height + offset > y > line_height - offset:
                print('检测到车辆')
                count += 1
                cars.remove((x, y))
    print(count)
    # 绘制检测结果文字
    cv2.putText(
        frame,
        f'car count: {count}',
        (20, 50),
        color=(0, 244, 0),
        thickness=2,
        fontFace=cv2.FONT_ITALIC,
        fontScale=1
    )

    #  展示视频图像和检测结果
    cv2.imshow('video frame', frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
