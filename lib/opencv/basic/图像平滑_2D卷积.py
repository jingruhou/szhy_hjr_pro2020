import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    图像平滑
    
    2D卷积 
    同一维信号一样，可以对2D图像实施低通滤波（LPF）和高通滤波（HPF）
    LPF用于去除噪音，模糊图像；HPF用于找到图像的边缘
    
    OpenCV提供的函数cv2.filter2D()可以对一幅图像进行卷积操作
    下面例子是使用5*5的平均滤波器，操作如下，将核放在图像的一个像素A上，求与核对应的图像上25（5*5）个像素的和，
    再取平均数，用这个平均数代替像素A的值。重复以上操作直到将图像的每一个像素值都更新一遍。
"""
img = cv2.imread('0.jpg')

kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('averaging')
plt.xticks([]), plt.yticks([])
plt.show()