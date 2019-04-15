import numpy as np
import cv2
import re
#  绘制画布
canvas = np.zeros((720,1280,3),dtype="uint8")

# 定义颜色
green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)

f = open('xml.txt', 'r')

# 用于存储需要绘制直线的三个点坐标 因为点坐标为数字 所以必须用数组
x = [0, 0, 0]
y = [0, 0, 0]

# 一次性读取所有的内容 节省时间
line = f.readlines()
# print(line)
# print(line[0])

# 设置循环初始状态
i=0
n=0
m = len(line)
# print(m)

# 将行数设置为外循环条件
while(m > 0):
    # 设置每次读取三行后进行处理
    for i in range(n,n+3):
        # print(i)
        # print(n,n+3)
        r = re.split(' ',line[i])
        m -= 1
        print(i)
        print(r)
        r[0] = float(r[0])
        r[1] = float(r[1])
        r[2] = float(r[2])
        r[3] = float(r[3])
        # 因为x只包含3个数 所以下标需要对3取余才不会越界
        x[i%3] = int((r[0]+r[2])/2)
        y[i%3] = int((r[1]+r[3])/2)
        # print(x)
        # print(y)
    # 将n重新赋值从而可以继续循环
    n = i + 1
    # print(n)
    # print(i)
    # 绘制线段 因为i的值最后为累加后的 所以做减法运算
    cv2.line(canvas,(x[(i-2)%3],y[(i-2)%3]),(x[(i-1)%3],y[(i-1)%3]),green)
    cv2.line(canvas,(x[(i-1)%3],y[(i-1)%3]),(x[i%3],y[i%3]),green)
    cv2.imwrite("traffic_line.jpg", canvas)

