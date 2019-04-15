# import cv2
#
# # 载入并显示图片
# img = cv2.imread('circles.jpg')
# # img = cv2.imread('circle.png')
# # img = cv2.imread('circles.jpg')
# # img=cv2.imread('circles.png')
# cv2.imshow('img', img)
# # 灰度化
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 输出图像大小，方便根据图像大小调节minRadius和maxRadius
# print(img.shape)
# # 霍夫变换圆检测
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=5, maxRadius=30)
# # 输出返回值，方便查看类型
# print(circles)
# # 输出检测到圆的个数
# print(len(circles[0]))
#
# print('-------------我是条分割线-----------------')
# # 根据检测到圆的信息，画出每一个圆
# for circle in circles[0]:
#     # 圆的基本信息
#     print(circle[2])
#     # 坐标行列
#     x = int(circle[0])
#     y = int(circle[1])
#     # 半径
#     r = int(circle[2])
#     # 在原图用指定颜色标记出圆的位置
#     img = cv2.circle(img, (x, y), r, (0, 0, 255), 1)
# # 显示新图像
# cv2.imshow('res', img)
#
# # 按任意键退出
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -*- coding: utf-8 -*-

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# img = cv2.imread('circles.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# plt.subplot(121), plt.imshow(gray, 'gray')
# plt.xticks([]), plt.yticks([])
#
# circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
#                             100, param1=100, param2=30, minRadius=5, maxRadius=300)
# print(circles1)
# circles = circles1[0, :, :]
# circles = np.uint16(np.around(circles))
# for i in circles[:]:
#     cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)
#     cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)
#     # cv2.rectangle(img, (i[0] - i[2], i[1] + i[2]), (i[0] + i[2], i[1] - i[2]), (255, 255, 0), 5)
#
# print("圆心坐标", i[0], i[1])
# plt.subplot(122), plt.imshow(img)
# plt.xticks([]), plt.yticks([])