import os

source_floder='/home/hjm/t/'
dest = '/home/hjm/t2.txt'

file_list = os.listdir(source_floder)
file_list = sorted(file_list)

obj = ""
for file in file_list:
    obj += file.strip('.jpg')+'\n'
    # print(obj)

with open(dest,'w') as w:
        w.write(obj)
w.close()