import numpy as np
import cv2
print(cv2.__version__)
"""
    OpenCV图像读取 显示 保存
"""

# 读取图片
img = cv2.imread('ld.jpg')

# 相关图像处理业务
# 结果展示
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 结果保存
cv2.imwrite('saveResult.png', img)

#########################################################

from matplotlib import pyplot as plt
img = cv2.imread('ld.jpg', 0)
plt.imshow(img,cmap='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
