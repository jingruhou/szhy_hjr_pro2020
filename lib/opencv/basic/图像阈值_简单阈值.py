import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    图像阈值
    
    cv2.threshold()
    
    当像素值高于阈值时，我们给个像素赋予一个新值（可能是白色），
    否则我们给它赋予另外一种颜色（也许是黑色）。
    
    这个函数第一个参数就是原图像，原图像应该是灰度图；第二个参数就是用来对像素值进行分类的阈值，
    第三个参数就是当像素值高于（或者小于）阈值时，应该被赋予新的像素值。
    OpenCV提供了多种不同的阈值方法，这是有第四个参数决定，方法包括：
        cv2.THRESH_BINARY
        cv2.THRESH_BINARY_INV
        cv2.THRESH_TRUNC
        cv2.THRESH_TOZERO
        cv2.THRESH_TOZERO_INV
"""
img = cv2.imread('0.jpg', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['original image', 'Binary', 'binary-inv', 'trunc', 'tozero', 'tozero-inv']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()