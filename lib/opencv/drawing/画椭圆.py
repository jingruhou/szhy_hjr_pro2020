import numpy as np
import cv2

"""
    OpenCV中的绘图函数

    涉及的函数包括：cv2.line(),cv2.cicle(),cv2.rectangle(),cv2.ellipse(),cv2.putText()等

    需要设置的参数：
    img 你想要绘制的图形的那副图像
    color 形状的颜色，以RGB为例，需要传入的元组，例（255，0，0）代表蓝色；对于灰度图只需要传入灰度值
    thickness 线条的粗细，如果给一个闭合图形设置为-1，那么这个图形就会被填充，默认值为1
    linetype 线条类型，8连线，抗锯齿等。默认是8连线。cv2.LINNE_AA为抗锯齿
"""

"""
    画椭圆
"""
img = np.zeros((512, 512, 3), np.uint8)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)

# 为了演示，建窗口显示出来
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1000, 1000)  # 定义frame的大小
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()