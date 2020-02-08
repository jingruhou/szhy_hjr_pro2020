import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
    透视变换
    
    对于视角变换，我们需要一个3*3变换矩阵。在变换前后直线还是直线。
    需要在原图上找到4个点，以及他们在输出图上对应的位置，这四个点中任意三个都不能共线，
    由函数cv2.getPerspectiveTransform()构建，然后这个矩阵传给函数cv2.warpPerspective()

"""
img = cv2.imread('1.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()