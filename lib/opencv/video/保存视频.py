import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# FourCC是一个4字节码，用来确定视频的编码格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 创建一个VideoWrite对象，确定输出文件名，
# 指定FourCC编码，播放频率，帧的大小
# 最后是isColor标签 True为彩色
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
