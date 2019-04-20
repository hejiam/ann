import os

source_path = '/home/hjm/darknet/data/lenet/version/'
dst_path = '/home/hjm/darknet/data/lenet/test/'

list = os.listdir(source_path)

for l in list:
    l = os.path.join(source_path,l)
    os.system('cp ' + l + '/* ' + dst_path)