import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
    几何变换设计的函数
    cv2.getPerspectiveTransform 透视变换
    cv2.warpAffine 仿射变换
    cv2.warpPersperctive  
"""

"""
    仿射变换
    
    仿射变换是一种二维坐标到二维坐标之间的线性变换，并保持二维图形的"平直性"。
    转换前平行的线，在转换后依然平行
    
    在仿射变换中，原图中所有平行线在结果图像中同样平行。
    为了创建这个矩阵，需要从原图像中找到三个点以及他们在输出图像中的位置，
    然后cv2.getAffineTransForm()会创建一个2*3的矩阵。
    最后这个矩阵会被传给函数cv2.warpAffine()
"""
img = cv2.imread('1.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# 行、列、通道数
M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()

# cv2.imshow('res', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
