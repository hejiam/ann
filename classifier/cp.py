# import os
#
# source_path = '/home/hjm/darknet/data/lenet/version/'
# dst_path = '/home/hjm/darknet/data/lenet/test/'
#
# list = os.listdir(source_path)
#
# for l in list:
#     l = os.path.join(source_path,l)
#     os.system('cp ' + l + '/* ' + dst_path)

# import os

# src_path = '/home/hjm/images/3/origin/version/'
# dst_path = '/home/hjm/images/3/origin/'
# dst1_path = '/home/hjm/images/3/origin/false_positive/'

# list1 = os.listdir(src_path)
# list2 = os.listdir(dst_path)

# for l1 in list1:
#     for l2 in list2:
#         if l1 == l2:
#             l1 = os.path.join(src_path, l1)+'/'
#             l2 = os.path.join(dst_path, l2)+'/'
#             os.system('cp ' + l1 + '* ' + l2)
#             break

# for l in list2:
#     if (l.find('lowest') > 0) | (l.find('remove') > 0) :
#         l = os.path.join(dst_path, l) + '/*'
#         os.system('mv ' + l + ' ' + dst1_path)

import os


src_path = '/home/hjm/images/3/origin/'
dst_path = '/home/hjm/images/3/valid/'

list = sorted(os.listdir(src_path))
print(list)

# s_path = os.path.join(src_path,list[0])+'/'
# list1 = os.listdir(s_path)
# # print(list1)
# d_path = os.path.join(dst_path,list[0])

# for i in range(0,3120,3):
#     os.system('mv '+ s_path+list1[i] + ' ' + d_path )

# s_path = os.path.join(src_path,list[1])+'/'
# list1 = os.listdir(s_path)
# print(list1)
# d_path = os.path.join(dst_path,list[1])
# for i in range(0,12,3):
#     os.system('mv ' + s_path + list1[i] + ' ' + d_path)

s_path = os.path.join(src_path,list[13])+'/'
list1 = os.listdir(s_path)
print(list1)
d_path = os.path.join(dst_path,list[13])
for i in range(0,1922,5):
    os.system('mv ' + s_path + list1[i] + ' ' + d_path)