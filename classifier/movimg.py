import os

# txt1_path = input('txt1_path: ')
# txt2_path = input('txt2_path: ')
# img_path = input('img_path: ')
# m1_path = input('m1_path: ')
# m2_path = input('m2_path: ')

txt1_path = '/home/hjm/darknet/correct.txt'
txt2_path = '/home/hjm/darknet/error.txt'
img_path = '/home/hjm/darknet/data/lenet/t/'
correct_path = '/home/hjm/darknet/data/lenet/correct/'
error_path = '/home/hjm/darknet/data/lenet/error/'

list = os.listdir(img_path)
list = sorted(list)

with open(txt1_path,'r') as r1:
    lines1 = r1.readlines()

with open(txt2_path,'r') as r2:
    lines2 = r2.readlines()

# for l in list:
#     # l = l + '\n'
#     for line in lines1:
#         line = line.split('\n')
#         # print(line)
#         # print(l)
#         if l == line[0]:
#             print(line[0])
#             os.system('cp '+img_path + l + ' ' + correct_path)


for l in list:
    for line in lines2:
        line = line.split('\n')
        if l == line[0]:
            print(line[0])
            os.system('cp ' + img_path + l + ' ' + error_path)
