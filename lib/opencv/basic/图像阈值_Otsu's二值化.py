import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    Otsu's二值化
    
    cv2.threshold函数是有两个返回值的，前面一直用的第二个返回值，
    也就是阈值处理后的图像，那么第一个返回值（得到的图像的阈值）将会在这里用到。
    
    前面对于阈值的处理上，我们选择的阈值都是127，那么实际情况下，怎么去选择这个127呢？
    有的图像可能阈值不是127得到的效果更好。那么我们需要算法自己去寻找到一个阈值，
    而Otsu's就可以自己找到一个认为最好的阈值。并且Otsu's非常适合图像灰度直方图具有双峰的情况，
"""
img = cv2.imread('0.jpg', 0)

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# (5, 5)为高斯核的大小，0为标准差
blur = cv2.GaussianBlur(img, (5, 5), 0)
# 阈值一定要设为0
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0, th1,
          img, 0, th2,
          img, 0, th3]
titles = ['original noise image', 'histogram', 'global thresholding(v=127)',
          'original noise image', 'histogram', "otsu's thresholding",
          'gaussian giltered image', 'histogram', "otus's thresholding"]

for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()