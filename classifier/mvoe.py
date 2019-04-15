# 将增强后存放于output中的数据移动到当前类别的数据集中
import os

source_path = '/home/hjm/images/2/o2/'

list = os.listdir(source_path)
list = sorted(list)

for l in list:
    l = os.path.join(source_path,l)
    # os.system("mv " + l + "/output/* " + l)
    # 可设置删除命令删除output文件夹
    os.system("rm -r " + l + "/output")

# import os
#
# # source_path = '/home/hjm/lenet_train/image_new/'
# source_path = '/home/hjm/lenet_train/image_old/'
#
# list = os.listdir(source_path)
# list = sorted(list)
#
# for l in list:
#     print(l)
#     # os.system("mv " + l + "/output/* " + l)
#     # 可设置删除命令删除output文件夹
#     l  = os.path.join(source_path,l)
#     os.system("rm -r " + l + "/output")



