# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import spline
# import cv2
#
#
#
# T = np.array([2,6,8])
# power = np.array([4,6,11])
# xnew = np.linspace(T.min(),T.max(),300)
#
# power_smooth = spline(T,power,xnew)
#
# # plt.plot(T,power)
# plt.plot(xnew,power_smooth)
# plt.show()

# from matplotlib import pyplot as plt
import numpy as np
import cv2
import re
canvas = np.zeros((720,1280,3),dtype="uint8")

green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)

f = open('xml.txt', 'r')

x = [0, 0, 0]
y = [0, 0, 0]

line = f.readlines()
# print(line)
# print(line[0])

i=0
n=0
m = len(line)
# print(m)

while(m >0):
    for i in range(n,n+3):
        # print(i)
        # print(n,n+3)
        r = re.split(' ',line[i])
        m -= 1
        print(r)
        r[0] = float(r[0])
        r[1] = float(r[1])
        r[2] = float(r[2])
        r[3] = float(r[3])
        x[i%3] = int((r[0]+r[2])/2)
        y[i%3] = int((r[1]+r[3])/2)
        print(x)
        print(y)
    n = i + 1
    # print(n)
    # print(i)
    cv2.line(canvas,(x[(i-2)%3],y[(i-2)%3]),(x[(i-1)%3],y[(i-1)%3]),green)
    cv2.line(canvas,(x[(i-1)%3],y[(i-1)%3]),(x[i%3],y[i%3]),green)
    cv2.imwrite("Canvas.jpg", canvas)


# file_data = ""
# for line[i] in f.readlines():
#     for i in range(n, n+3):
#         file_data += line
#         print(file_data)
    #     r = re.split(' ',line[i])
    #     # print(r)
    #     r[0] = float(r[0])
    #     r[1] = float(r[1])
    #     r[2] = float(r[2])
    #     r[3] = float(r[3])
    #     x[i] = int((r[0]+r[2])/2)
    #     y[i] = int((r[1]+r[3])/2)
    #     # print(x)
    #     # print(y)
    # cv2.line(canvas,(x[i-2],y[i-2]),(x[i-1],y[i-1]),green)
    # cv2.line(canvas,(x[i-1],y[i-1]),(x[i],y[i]),green)
    # cv2.imwrite("Canvas.jpg", canvas)
    # n=i+1
    # print(n)


# cv2.line(canvas,(x[0],y[0]),(x[1],y[1]),green)
# cv2.line(canvas,(x[1],y[1]),(x[2],y[2]),green)
# cv2.imwrite("Canvas.jpg", canvas)
    # n=i

# cv2.line(canvas,(0,0),(300,300),green)
# cv2.line(canvas,(300,300),(389,354),green)

# cv2.imwrite("Canvas.jpg",canvas)
# plt.imshow(canvas[:,:,::-1])
# plt.show()