import cv2
import numpy as np

"""
    颜色空间转换

    在OpenCV中有超过150种进行颜色空间转换的方法。
    常用的就两种：BGR-Gray和BGR-HSV
    
    我们用到的函数是cv2.cvtColor(input_imageflag),其中flag就是转换类型
    对于BGR-Gray的转换，我们使用的flag就是cv2.COLOR_BGR2GRAY。
    对于BGR-HSV 的转换，我们使用的flag就是cv2.COLOR_BGR2HSV。

    在OpenCV的HSV格式中，H(色彩/色度)的取值范围是[0， 179]，S(饱和度)的取值范围[0， 255]V(亮度)的取值范围[0， 255]。
    注意：不同的软件使用的值可能不同，所以当你拿OpenCV的HSV值与其他软件的HSV值对比，一定记得"归一化"
"""

"""
    物体跟踪
    
    步骤：
    【1】从视频中获取每一帧图像
    【2】将图像转化为HSV空间
    【3】设置HSV阈值到蓝色范围
    【4】获取蓝色物体-当然我们也可以做其他任何我们想做的事情，比如在蓝色物体周围画一个圈
"""
# cap = cv2.VideoCapture(0)
#
# while 1:
#     # 获取每一帧
#     ret, frame = cap.read()
#     # 转化到HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     # 设定蓝色的阈值
#     lower_blue = np.array([110, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     # 根据阈值构建掩码
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#     # 对原图和掩码进行位运算
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#
#     # 显示图像
#     cv2.imshow('frame', frame)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# # 关闭窗口
# cv2.destroyAllWindows()

"""
    怎样找到跟踪对象的HSV值
    
    函数cv2.cvtColor()可以用到这里，需要传入的参数是值，而不是一幅图

    np.uint8([[[0, 255, 0]]]) 不能用 [0,255,0] ,
    而用 [[[0,255,0]]] 的三层括号应分别对应于 
    cvArray cvMat IplImage
"""
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)  # [[[ 60 255 255]]]
