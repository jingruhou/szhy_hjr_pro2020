import cv2

"""
    几何变换设计的函数
    cv2.getPerspectiveTransform 透视变换
    cv2.warpAffine 仿射变换
    cv2.warpPersperctive  
"""

"""
    平移
    
    函数cv2.warpAffine()的第三个参数是输出图像的大小
    它的格式应该是图像的（宽， 高）。
    应该记住的是图像的宽对应的是列数，高对应的是行数
"""
"""
    旋转
    
    OpenCV提供函数cv2.getRotationMatrix2D构建旋转矩阵
"""
img = cv2.imread('1.jpg', 0)
rows, cols = img.shape
# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可用通过设置旋转中心，缩放因子以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (2*cols, 2*rows))

while 1:
    cv2.imshow('img', dst)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()