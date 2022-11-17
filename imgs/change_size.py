import cv2


def changeSize(path, scale):
    img = cv2.imread(path)
    result = cv2.resize(img, None, fx=scale, fy=scale)
    return result

if __name__ == '__main__':
    img_path = 'beach-work.jpg'
    result = changeSize(img_path, 0.5)
    cv2.imwrite('dst.jpg', result)
