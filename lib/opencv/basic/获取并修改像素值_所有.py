import cv2
import numpy as np

"""
    numpy是经过优化了的进行快速矩阵运算的包，所以不推荐逐个获取像素值并修改
    能矩阵运算就不要用循环
"""
img = cv2.imread('1.jpg')
print(img.item(100, 100, 2))  # 获取100行100列的B通道的像素值（blue值） 118

img.itemset((100, 100, 2), 100)
print(img.item(100, 100, 2))

