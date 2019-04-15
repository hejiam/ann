# 将数据集按照一定的比例放入test和train数据集中
import os
#
# source_path = '/home/hjm/darknet/data/test1/traffic_sign_20/'
# file2_path = '/home/hjm/darknet/data/lenet/test/'
# file3_path = '/home/hjm/darknet/data/lenet/train/'
#
# for i in range(0,10):
#     l = os.path.join(source_path,list[i])
#     print (list[i])
#     os.system("mv " + l + " " + file2_path)
#     i +=1
# os.system("mv " + source_path + "/* " + file3_path)

# source_path = '/home/hjm/images/2/o2/'
# file2_path = '/home/hjm/darknet/data/lenet1/test/'
# file3_path = '/home/hjm/darknet/data/lenet1/train/'

source_path = '/home/hjm/traffic_valid/valid/t_sign/'
# file2_path = '/home/hjm/darknet/data/lenet1/test/'
file3_path = '/home/hjm/darknet/data/lenet/valid/'

list = os.listdir(source_path)

for l in list:
    picture_path = os.path.join(source_path,l)
    picture_list = os.listdir(picture_path)
    # for i in range(0,400):
    #     p = os.path.join(picture_path,picture_list[i])
    #     print(picture_list[i])
    #     os.system("mv " + p + " " + file2_path)
    #     i += 1
    # list = os.listdir(source_path)
    # print("\n")
    # print(list)
    os.system("mv " + picture_path + "/* " + file3_path)

