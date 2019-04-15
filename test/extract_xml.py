
# -*- coding:utf-8 -*-


import xml.dom.minidom
import os
import argparse

parse=argparse.ArgumentParser()
parse.add_argument('-o','--object')
args=parse.parse_args()
object=args.object


xml_name=object
txt_name=os.path.splitext(xml_name)[0]
DOMTree = xml.dom.minidom.parse(xml_name)
collection = DOMTree.documentElement



# 寻找以<object>开始内容
objects=collection.getElementsByTagName("object")
# 计算object个数
objects_num=len(objects)
print(objects_num)



# f = open(txt_name+'.txt', 'w')
# f.writelines(str(objects_num)+'\n')
f = open('xml.txt','w')



for object in objects:
   print("*****Object*****")
   bndbox = object.getElementsByTagName('bndbox')[0]
   xmin = bndbox.getElementsByTagName('xmin')[0]
   xmin_data=xmin.childNodes[0].data
   print (xmin_data)
   ymin = bndbox.getElementsByTagName('ymin')[0]
   ymin_data=ymin.childNodes[0].data
   print (ymin_data)
   xmax = bndbox.getElementsByTagName('xmax')[0]
   xmax_data=xmax.childNodes[0].data
   print (xmax_data)
   ymax = bndbox.getElementsByTagName('ymax')[0]
   ymax_data=ymax.childNodes[0].data
   print (ymax_data)

   # 将查找的内容写入到.txt文件中
   f.writelines(str(xmin_data)+' '+str(ymin_data)+' '+str(xmax_data)+' '+str(ymax_data)+'\n')


f.close()
