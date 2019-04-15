import os
from os import listdir,getcwd
from os.path import join

if __name__ == '__main__':
    # 地址是所有图片的保存地点
    source_folder='/home/hjm/VOCdevkit/VOC2007/JPEGImages/'
    # 保存train.txt的地址
    dest = '/home/hjm/VOCdevkit/VOC2007/train_2007.txt'
    dest1 = '/home/hjm/VOCdevkit/VOC2007/filelist/train_2007.txt'
    # 赋值图片所在文件夹的文件列表
    file_list = os.listdir(source_folder)
    # 打开文档train.txt
    train_file = open(dest,'a')
    train_file1 = open(dest1,'a')
    # 访问文件列表中的每一个文件
    for file_obj in file_list:
        # 将全部给定的path片段拼接在一起
        file_path = os.path.join(source_folder,file_obj)
        # file_name保存文件的名字 file_extend保存文件扩展名 os.path.splitext()分离文件名和扩展名
        file_name,file_extend = os.path.splitext(file_obj)
        # file_num = int(file_name)
        train_file.write(file_name+'\n')
        train_file1.write(file_path+'\n')
    # 关闭文件
    train_file.close()


# sorted train.txt
train_data = []
with open('train_2007.txt', 'r') as f:
    for line in f:
        # str.strip() 移除字符串首尾指定的字符生成新的字符串,为空时默认删除空白符（'\n','\t','\r',''）
        # train_data.append(line) 与下面表达式相等
        train_data.append(line.strip()+'\n')
f.close()

with open('train_2007.txt', 'w') as w:
    # sorted()按字典序进行排序
    for item in sorted(train_data):
        # write()必须是字符 不能是列表
        w.write(item)
w.close()