import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np
import re


# 图片存储路径
src_img_dir = '/home/hjm/traffic_valid/t_valid/'
# src_img_dir = '/home/hjm/traffic_valid/traffic_valid/'
# txt文件存储路径
src_txt_sir = '/home/hjm/traffic_valid/traffic_valid.txt'
# xml文件存储路径
src_xml_dir = '/home/hjm/traffic_valid/Annotations1/'


# labels = os.listdir(src_txt_sir)
# names文件的路径
clsnames_path = '/home/hjm/traffic_valid/name.names'

#  读取分类名字
with open(clsnames_path,'r') as f:
    classes = f.readlines()
    classes = [cls.strip('\n') for cls in classes]

# 按照格式将.txt的内容转换成.xml


def write_xml(imgname, filepath, labeldicts):                                # 参数imagename是图片名（无后缀） filepath为文件路径名
    root = ET.Element('Annotation')                                          # 创建Annotation根节点
    ET.SubElement(root, 'folder').text = 'traffic_sign'                      # 创建filename子节点（无后缀）
    ET.SubElement(root, 'filename').text = str(imgname)                      # 创建filename子节点（无后缀）
    ET.SubElement(root, 'path').text = src_img_dir + imgname +'.jpg'         # 创建filename子节点（无后缀）
    source = ET.SubElement(root,'source')                                    # 创建source根节点
    ET.SubElement(source, 'database').text = 'Unknown'

    sizes = ET.SubElement(root,'size')                                        # 创建size子节点
    ET.SubElement(sizes, 'width').text = '1280'                               # 图像的尺寸大小：img.shape[0], img.shape[1]
    ET.SubElement(sizes, 'height').text = '720'
    ET.SubElement(sizes, 'depth').text = '3'                                  # 图片的通道数：img.shape[2]
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')                               # 创建object子节点
        ET.SubElement(objects, 'name').text = labeldict['name']               # 目标检测图像的类别名
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        # a = labeldict['xmin']
        # int(float(a))
        ET.SubElement(bndbox, 'xmin').text = str(int(float(labeldict['xmin'])))
        ET.SubElement(bndbox, 'ymin').text = str(int(float(labeldict['ymin'])))
        ET.SubElement(bndbox, 'xmax').text = str(int(float(labeldict['xmax'])))
        ET.SubElement(bndbox, 'ymax').text = str(int(float(labeldict['ymax'])))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')


# 读取.txt文件
with open(src_txt_sir, 'r') as r:
    for line in r.readlines():
        # 将一行中的文字按空格分开存储在s1中 但是文字的类型为字符型
        s1 = re.split(' ', line)
        img_id = s1[0]
        img = np.array(Image.open(src_img_dir + img_id + '.jpg'))
        # print(s1[0])
        # print(img_id)
        # contents = f.readlines()
        labeldicts = []
        # for content in contents:
        img = np.array(Image.open(src_img_dir + img_id + '.jpg'))
        sh, sw = img.shape[0], img.shape[1]                   # img.shape[0]是图片的高度 img.shape[1]是图片的宽度
        new_dict = {'name': classes[0],
                    'difficult': '0',
                    'xmin': s1[2],   # 类型为字符型 转为整型需要先转浮点型再转整型
                    'ymin': s1[3],
                    'xmax': s1[4],
                    'ymax': s1[5]
                    }
        labeldicts.append(new_dict)
        write_xml(img_id, src_xml_dir + img_id + '.xml', labeldicts)