import cv2
import numpy as np

"""
    检测程序效率
    
    cv2.getTickCount函数返回从参考点到这个函数被执行的时钟数
    在一个函数执行前后都调用它，可以得到这个函数的执行时间
    
    cv2.getTickFrequency函数返回时钟频率，或者说每秒钟的时钟数
    例，窗口大小不同（5，7，9）的核函数来做中值滤波，查看一个函数运行了多少秒
"""
img1 = cv2.imread('1.jpg')
e1 = cv2.getTickCount()

for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)

"""
    OpenCV中的默认优化
    
    cv2.useOptimized()来查看优化是否被开启
    cv2.setUesOptimized()来开启优化
"""
cv2.setUseOptimized(True)

res = cv2.medianBlur(img1, 49)
print(res)

cv2.setUseOptimized(False)

res = cv2.medianBlur(img1, 49)
print(res)