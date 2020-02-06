import cv2
import numpy

img = cv2.imread('1.jpg')
# img.shape可以获得图像的形状，返回值是一个包含行数、列数、通道数的元组
print(img.shape)  # (212, 347, 3)

# img.size可以返回图像的像素数目
print(img.size)  # (212, 347, 3)

# img.dtype返回图像的数据类型
print(img.dtype)  # uint8
