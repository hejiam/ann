# import os
#
# t1_floder = '/home/hjm/t1/'
# source_floder = '/home/anngic/dataset/data_anngic/traffic_sign/t/'
# txt_floder = '/home/hjm/test.txt'
#
# file_list=os.listdir(t1_floder)
# file_list = sorted(file_list)
# txt = open(txt_floder,'w')
#
# file_data = ""
#
# for file in file_list:
#     file_data +=source_floder+file+'\n'
#
# txt.write(file_data)
# txt.close()

# import os
# import xml.etree.ElementTree as ET
# from PIL import Image
# import numpy as np
#
# img_path = '/home/hjm/traffic_valid/t/'                   #原图.jpg文件的路径
# labels_path = '/home/hjm/traffic_valid/labels/'                    #labels中.txt文件的路径
# annotations_path = '/home/hjm/trffic_valid/Annotations/'          #生成的xml文件需要保存的路径
# labels = os.listdir(labels_path)
# clsnames_path = '/home/hjm/traffic_valid/name.names'     #names文件的路径
#
# with open(clsnames_path,'r') as f:
#     classes = f.readlines()
#     classes = [cls.strip('\n') for cls in classes]
#
# def write_xml(imgname,filepath,labeldicts):                     #参数imagename是图片名（无后缀）
#     root = ET.Element('Annotation')                             #创建Annotation根节点
#     ET.SubElement(root, 'filename').text = str(imgname)         #创建filename子节点（无后缀）
#     sizes = ET.SubElement(root,'size')                          #创建size子节点
#     ET.SubElement(sizes, 'width').text = '1280'                 #没带脑子直接写了原图片的尺寸......
#     ET.SubElement(sizes, 'height').text = '720'
#     ET.SubElement(sizes, 'depth').text = '3'                    #图片的通道数：img.shape[2]
#     for labeldict in labeldicts:
#         objects = ET.SubElement(root, 'object')                 #创建object子节点
#         ET.SubElement(objects, 'name').text = labeldict['name']        #BDD100K_10.names文件中
#                                                                        #的类别名
#         ET.SubElement(objects, 'pose').text = 'Unspecified'
#         ET.SubElement(objects, 'truncated').text = '0'
#         ET.SubElement(objects, 'difficult').text = '0'
#         bndbox = ET.SubElement(objects,'bndbox')
#         ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
#         ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
#         ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
#         ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
#     tree = ET.ElementTree(root)
#     tree.write(filepath, encoding='utf-8')
#
#
# for label in labels:                                           #批量读.txt文件
#     with open(labels_path + label, 'r') as f:
#         img_id = os.path.splitext(label)[0]
#         contents = f.readlines()
#         labeldicts = []
#         for content in contents:
#             img = np.array(Image.open(img_path+label.strip('.txt') + '.jpg'))
#             sh,sw = img.shape[0],img.shape[1]                  #img.shape[0]是图片的高度720
#                                                                #img.shape[1]是图片的宽度720
#             content = content.strip('\n').split()
#             x=float(content[1])*sw
#             y=float(content[2])*sh
#             w=float(content[3])*sw
#             h=float(content[4])*sh
#             new_dict = {'name': classes[int(content[0])],
#                         'difficult': '0',
#                         'xmin': x+1-w/2,                      #坐标转换公式看另一篇文章....
#                         'ymin': y+1-h/2,
#                         'xmax': x+1+w/2,
#                         'ymax': y+1+h/2
#                         }
#             labeldicts.append(new_dict)
#         write_xml(img_id, annotations_path + label.strip('.txt') + '.xml', labeldicts)

# import re
# f = open("0.txt")
# s = f.read()
# 读取一行中以空格分开的各个内容
# s1 = re.split(' ',s)
# print(s1[0])
# print(s1[1])
# print(s1[2])
# print(s1[3])
#
# for i in s1:
#     print (i)

import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np
import re


# 图片存储路径
src_img_dir = '/home/hjm/traffic_valid/valid/valid/'
# src_img_dir = '/home/hjm/traffic_valid/traffic_valid/'
# txt文件存储路径
src_txt_sir = '/home/hjm/traffic_valid/valid/traffic_valid.txt'
# src_txt_sir = '/home/hjm/traffic_valid/traffic_valid.txt'
# xml文件存储路径
src_xml_dir = '/home/hjm/traffic_valid/valid/Annotations/'
# src_xml_dir = '/home/hjm/traffic_valid/Annotations/'


# labels = os.listdir(src_txt_sir)

clsnames_path = '/home/hjm/traffic_valid/name.names'     #names文件的路径

#  读取类名字
with open(clsnames_path,'r') as f:
    classes = f.readlines()
    classes = [cls.strip('\n') for cls in classes]


def write_xml(imgname,filepath,labeldicts):                     #参数imagename是图片名（无后缀）
    root = ET.Element('Annotation')                             #创建Annotation根节点
    ET.SubElement(root, 'folder').text = 'traffic_sign'  # 创建filename子节点（无后缀）
    ET.SubElement(root, 'filename').text = str(imgname)         #创建filename子节点（无后缀）
    ET.SubElement(root, 'path').text = src_img_dir + imgname +'.jpg'         #创建filename子节点（无后缀）
    source = ET.SubElement(root,'source')                          #创建source子节点
    ET.SubElement(source, 'database').text = 'Unknown'

    sizes = ET.SubElement(root,'size')                          #创建size子节点
    ET.SubElement(sizes, 'width').text = '1280'                 #没带脑子直接写了原图片的尺寸......
    ET.SubElement(sizes, 'height').text = '720'
    ET.SubElement(sizes, 'depth').text = '3'                    #图片的通道数：img.shape[2]
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')                 #创建object子节点
        ET.SubElement(objects, 'name').text = labeldict['name']        #BDD100K_10.names文件中
                                                                       #的类别名
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        a = labeldict['xmin']
        int(float(a))
        ET.SubElement(bndbox, 'xmin').text = str(int(float(labeldict['xmin'])))
        ET.SubElement(bndbox, 'ymin').text = str(int(float(labeldict['ymin'])))
        ET.SubElement(bndbox, 'xmax').text = str(int(float(labeldict['xmax'])))
        ET.SubElement(bndbox, 'ymax').text = str(int(float(labeldict['ymax'])))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')


# 读.txt文件
with open(src_txt_sir, 'r') as r:
    for line in r.readlines():
        s1 = re.split(' ', line)
        img_id = s1[0]
        img = np.array(Image.open(src_img_dir + img_id + '.jpg'))
        print(s1[0])


    # print(img_id)
    # contents = f.readlines()
        labeldicts = []
    # for content in contents:
        img = np.array(Image.open(src_img_dir+ img_id + '.jpg'))
        sh,sw = img.shape[0],img.shape[1]                  #img.shape[0]是图片的高度720
                                                       #img.shape[1]是图片的宽度720\
        new_dict = {'name': classes[0],
                    'difficult': '0',
                    'xmin': s1[2],
                    'ymin': s1[3],
                    'xmax': s1[4],
                    'ymax': s1[5]
                    }
        labeldicts.append(new_dict)
        write_xml(img_id, src_xml_dir + img_id + '.xml', labeldicts)

    # content = content.strip('\n').split()
    # x=float(content[1])*sw
    # y=float(content[2])*sh
    # w=float(content[3])*sw
    # h=float(content[4])*sh
