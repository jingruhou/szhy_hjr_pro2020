"""
    使用摄像头捕获视频
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # 颜色空间转换: BGR转化为灰度图
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.cv2.imshow('frame', frame)
    # cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
