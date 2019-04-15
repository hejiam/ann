import cv2
import numpy as np
import sys
import os

file_path = '/home/hjm/traffic_valid/t_valid/'
list = os.listdir(file_path)

for l in list:
    name = os.path.splitext(l)[0]
    path = os.path.join(file_path,l)
    # print(name)
    im = cv2.imread(path)
    im = np.array(im)
    im  = im[:,:,[0,2,1]]
    cv2.imwrite("/home/hjm/traffic_valid/t_valid//%s.jpg" % name, im)