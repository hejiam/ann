import os

# file_path = "/home/hjm/sign/test/"
file_path = input("file_path: ")
# file_path = "/home/hjm/lenet_train/images/"
# anno_path = "/home/hjm/sign/testxml/"
anno_path = input("anno_path: ")
# anno_path = "/home/hjm/lenet_train/test/"

list = os.listdir(file_path)
list = sorted(list)

anno_list = os.listdir(anno_path)
anno_list = sorted(anno_list)
print(list)

file = ""

with open("a.txt",'w') as w:
    for l in list:
        # src = file_path + l
        l = l.strip(".png")+'\n'
        # file += l
        w.write(l)

w.close()
    # print(file)

with open('a.txt','r') as r:
    line = r.readlines()
    line = sorted(line)
    m = len(line)
    print(m)
# r.close()

i=0
while(m>0):
    for a in anno_list:
        src = os.path.join(anno_path,a)
        print(src)
        line[i]=line[i].strip()
        dst = anno_path + line[i] +".xml"
        os.rename(src,dst)
        i += 1
        m -= 1
r.close()
# import os
# import shutil
#
# file_path = '/home/hjm/lenet_train/t/'
# # file_path = '/home/hjm/lenet_train/test/'
# path = '/home/hjm/lenet_train/test/'
# # path = '/home/hjm/lenet_train/t/'
# list = os.listdir(file_path)
# list = sorted(list)
#
# i=0
# m=1768
# for l in list:
#     if m > 0:
#         src = os.path.join(file_path,l)
#         dst = os.path.join(path,l)
#         shutil.move(src, dst)
#     m -= 1
#     print(m)