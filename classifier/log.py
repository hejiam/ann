import os

source_path = '/home/hjm/darknet/name.log'

with open(source_path,'r') as r:
    lines = r.readlines()

i = 3
m = len(lines)+1
# print(m)

for i in range(3,m,2):
    # print (i)
    l1 = lines[i-2].split(',')[0].split(':')[2]
    l2 = lines[i].split(',')[0].split(':')[2]
    if l1>l2:
        
    # print(l1)

    # for line in lines:


# print(line)