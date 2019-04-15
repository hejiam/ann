# 生成（图像名）.txt文件 文件中包含这图像中目标的位置和类别标签
# xml文件使用labelImg标注图像 会自动生成相关标签的xml文件
# 输入为xml文件 输出为每张图像中包含的类别及类别的位置信息 即标签
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir,getcwd
from os.path import join

# 类别修改为自己需要检测的所有类别
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat",
           "chair", "cow", "diningtable", "dog",  "horse", "motorbike", "person",
           "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    # 与图片对应的xml文件所在的地址
    in_file = open('/home/hjm/VOCdevkit/VOC2007/Annotations/%s.xml'%(image_id))
    # 与此xml对应的转换后的txt 这个txt保存完整路径
    out_file = open('/home/hjm/VOCdevkit/VOC2007/labels/%s.txt'%(image_id),'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    # 访问size标签的数据
    size = root.find('size')
    # 读取size标签中宽度的数据
    w = int(size.find('width').text)
    # 读取size标签中高度的数据
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text    # 没设置difficult,所以屏蔽
        cls = obj.find('name').text
        if cls not in classes:  # or int(difficult) ==1
            continue
        cls_id = classes.index(cls)
        print(cls_id)
        # 访问boundbox标签的数据并进行处理 都按yolo自带的代码来 没有改动
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),float(xmlbox.find('ymin').text),float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

image_ids = open('/home/hjm/VOCdevkit/VOC2007/train_2007.txt').read().strip().split()
list_file = open('/home/hjm/VOCdevkit/VOC2007/train.txt','w')
for image_id in image_ids:
    # 将每一个用于训练和验证的图片的完整路径写入到.txt文件中 这个文件会被voc.data yolo.c调用
    list_file.write('/home/hjm/VOCdevkit/VOC2007/JPEGImages/%s.jpg'%(image_id)+'\n')
    # 将图片的名称id传给函数，用于把此图片对应的xml中的数据转换成yolo要求的txt格式
    convert_annotation(image_id)
list_file.close()