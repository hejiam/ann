import os

# source1_path = '/home/hjm/images/train/'
# source2_path = '/home/hjm/images/test/'
train_path = '/home/hjm/darknet/data/lenet/train/'
test_path = '/home/hjm/darknet/data/lenet/test/'

file1_path = '/home/hjm/darknet/data/lenet/train.list'
file2_path = '/home/hjm/darknet/data/lenet/test.list'

# file1_list = os.listdir(source1_path)
# file1_list = sorted(file1_list)
# file2_list = os.listdir(source2_path)
# file2_list = sorted(file2_list)

file1_list = os.listdir(train_path)
file1_list = sorted(file1_list)
file2_list = os.listdir(train_path)
file2_list = sorted(file2_list)


with open(file1_path,'a') as w:
    for f in file1_list:
        path = train_path + f +'\n'
        w.write(path)

with open(file2_path,'a') as w:
    for f in file2_list:
        path = test_path + f +'\n'
        w.write(path)