import os


# labels_path = '/home/hjm/traffic_valid/'
# labels_path = input('labels_path: ')
# transform_path = '/home/hjm/traffic_valid/'
# transform_path = input('transform_path: ')

# data = ''

# with open(labels_path, 'r') as r:
# # with open(file1_path, 'r') as r:
#     lines = r.readlines()
#     for line in lines:
#         line = line.split(" ")  # ['00001_235.jpg','u_80\n']
#         # print(line)
#         name = line[0].split("_")[0]
#         # print(name)
#         labels = line[1].split("_")
#         print(labels)
#         if labels[0] == 'u':
#             labels = name + '_traffic_sign_'+labels[1]
#             # print(labels)
#         elif labels[0] == 'r':
#             labels = name + '_traffic_sign_remove_'+labels[1]
#         elif labels[0] == 'l':
#             labels = name + '_traffic_sign_lowest_'+labels[1]
#         if labels[0] == 'f\n':
#             labels = name + '_false_positive\n'
#         data += labels
#         # print(labels)
# # print(data)
# r.close()

# with open(transform_path, 'w') as w:
#     w.write(data)
# w.close()



label_path = '/home/hjm/traffic_valid/t_test/labels.txt'
rename_path = '/home/hjm/traffic_valid/t_test/traffic_sign/'
# rename_path = '/home/hjm/darknet/data/lenet/new_valid/'
# rename_path = '/home/hjm/traffic_valid/test/'
list = sorted(os.listdir(rename_path))
n =len(list)
# print(list)

# with open(label_path, 'r') as r:
#     lines = r.readlines()
#     for l in list:
#         # src = os.path.join(file3_path, l)
#         l1 = l.split('.')
#         for line in lines:
#             l2 = line.split(' ')
#             if l1[0] == l2[0]:
#                 line = l1[0].split('_')[0]+'_'+l2[1].split('\n')[0]
#                 print(l2[1].split('\n'))
#                 print(line)
#                 src = os.path.join(rename_path,l)
#                 dst = rename_path + line + '.jpg'
#                 os.rename(src, dst)
# r.close()

with open(label_path, 'r') as r:
    lines = r.readlines()
    i = 0
    for i in range(0, n):
        l1 = lines[i].split(' ')
        l2 = list[i].split('.')
        if l1[0] == l2[0]:
            line = l1[0].split('_')[0]+'_'+l1[1].split('\n')[0]
            print(line)
            src = os.path.join(rename_path, list[i])
            dst = rename_path + line + '.jpg'
            os.rename(src, dst)
            i += 1
r.close()





# for l in list:
#     line = l.split('.jpg')[0].split('\n')[0]
#     # print(l)
#     src = os.path.join(rename_path,l)
#     dst = rename_path + line + '.jpg'
#     os.rename(src,dst)
