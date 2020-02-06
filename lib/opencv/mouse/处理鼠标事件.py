import numpy as np
import cv2

# 查看所有被支持的鼠标事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def draw_circle(event, x, y, flags, param):
    """
    鼠标回调函数
    :param event:
    :param x:
    :param y:
    :param flags:
    :param param:
    :return:
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()