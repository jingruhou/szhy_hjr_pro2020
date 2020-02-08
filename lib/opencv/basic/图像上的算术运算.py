import cv2
import numpy as np

"""
    图像加法
    
    使用cv2.add()将两幅图像进行加法运算，
    也可以直接使用numpy，res=img1+img2.两幅图像的大小、类型必须一致，或者第二个图像可以是一个简单的标量值

    openCV的加法是一种饱和操作，而numpy的加法是一种模操作
"""
x = np.uint8([250])
y = np.uint([10])
# print(cv2.add(x, y))
# print(x + y)

"""
    图像混合
    
    也是加法，不同的是两幅图像的权重不同，这会给人一种混合或者透明的感觉
    图像混合的计算公式如下：
    g(x) = (1−α)f0 (x)+αf1 (x)
    通过修改α的值（0 - 1），可以实现很酷的混合。
    
    例如，将两幅图像混合，第一幅权重为0.7，第二幅权重为0.3。
    函数cv2.addWeighted()可以按照下面的公式对图片进行混合
    dst = α·img1 + β·img2 + γ
    这里的γ的取值为0
"""
img1 = cv2.imread('2.jpg')
img2 = cv2.imread('3.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    图像的按位运算
    
    这里包括按位运算操作有：AND,OR,NOT,XOR等
    当我们提取图像的一部分时，选择非矩形ROI时，会很有用。
"""
img1 = cv2.imread('2.jpg')
img2 = cv2.imread('3.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 取ROI中与mask中不为零的值对应的像素的值，其让值为0.
# 注意这里必须有mask = mask或者mask = mask_inv,其中mask=不能忽略
img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()