import numpy as np
import cv2
import re
canvas = np.zeros((720,1280,3),dtype="uint8")

f = open('xml.txt','r')

for line in f.readlines():
    r = re.split(' ',line)
    r[0]=int(float(r[0]))
    r[1]=int(float(r[1]))
    r[2]=int(float(r[2]))
    r[3]=int(float(r[3]))
    # 绘制矩形
    cv2.rectangle(canvas,(r[0],r[1]),(r[2],r[3]), (0,255,0),1)
    cv2.imwrite("Canvas.jpg",canvas)

# cv2.writeKey(0)