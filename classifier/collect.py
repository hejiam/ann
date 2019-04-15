# 将image_lenet中相同类别的数据放入现有数据集中
import os

source_path = '/home/hjm/images/2/o2/'
file1_path = '/home/hjm/lenet_train/image_new/'
file2_path = '/home/hjm/lenet_train/image_old/'
file3_path = '/home/hjm/lenet_train/image_lenet/'
#
list = os.listdir(source_path)
list1 = os.listdir(file1_path)
list2 = os.listdir(file2_path)
list3 = os.listdir(file3_path)

# for l in list:
#     # print(l)
#     for l1 in list1:
#         # print(l1)
#         if l==l1:
#             # print(l1)
#             l = os.path.join(source_path, l)
#             l1 = os.path.join(file1_path, l1)
#             # print(l)
#             os.system("cp " + l1 + "/* " + l + "/" )
#
# for l in list:
#     # print(l)
#     for l2 in list2:
#         # print(l1)
#         if l==l2:
#             # print(l2)
#             l = os.path.join(source_path, l)
#             l2 = os.path.join(file2_path, l2)
#             # print(l)
#             os.system("cp " + l2 + "/* " + l + "/" )

for l in list:
    # print(l)
    for l3 in list3:
        # print(l1)
        if l==l3:
            # print(l2)
            l = os.path.join(source_path, l)
            l3 = os.path.join(file3_path, l3)
            # print(l)
            os.system("cp " + l3 + "/* " + l + "/" )