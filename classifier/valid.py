import os
#
# source_path = '/home/hjm/traffic_valid/t_test/version/'
#
# list = os.listdir(source_path)
# list = sorted(list)
# # print(list)
#
# data = ''
# with open('valid.list','w') as w:
#     for l in list:
#         img_path = os.path.join(source_path,l)+'/'
#         list2 = sorted(os.listdir(img_path))
#         print(list2)
#         for l2 in list2:
#             l2 = l2+'\n'
#             data += l2
#     w.write(data)





# file_path = '/home/hjm/darknet/data/lenet/test.list'
#
# with open('valid.list','r') as r1:
#     line1 = r1.readlines()
# r1.close()
#
# with open(file_path,'r') as r2:
#     line2 = r2.readlines()
# r2.close()
#
# data = ''
# for l1 in line1:
#     # print(l1)
#     for l2 in line2:
#         l2 = l2.split('/')[7]
#         # print(l2)
#         if l1 == l2:
#             # print('yes')
#             l1 = ''
#     data += l1
#
# with open('difference.list','w') as w:
#     w.write(data)
# w.close()

source_path = '/home/hjm/images/2_v1/o2/'

list = os.listdir(source_path)

data = ''
for l in list:
    file_path = os.path.join(source_path,l)+'/'
    file_list = os.listdir(file_path)
    for f in file_list:
        data += file_path + f+'\n'

with open('valid.txt','w') as w:
    w.write(data)

# source_path = '/home/hjm/traffic_valid/t_test/traffic_sign/'
#
# data = ''
# with open('difference.list', 'r') as r:
#     lines = r.readlines()
#     for line in lines:
#         line = source_path+line
#         data += line
# r.close()
#
# with open('difference.list', 'w') as w:
#     w.write(data)
