import os
import matplotlib.pyplot as plt


source_path = input("your address:")
# source_path = '/home/hjm/darknet/name.log'

with open(source_path,'r') as r:
    lines = r.readlines()

i = 3
m = len(lines)+1
# print(m)
# l = lines[1].split(',')[0].split(':')[2]
# print(l)
# if lines[1].split(',')[0].split(':')[2] == ' 1.000000':
#     line = lines[0].split(',')[0].split('/')[-1]
#     print(line)

data_correct = ''
data_error = ''
data = ''

if lines[1].split(',')[0].split(':')[2] == ' 1.000000':
    line = lines[0].split(',')[0].split('/')[-1]+'\n'
    # print(line)
    data_correct +=line
    data += line
    # w1.write(line)
elif lines[1].split(',')[0].split(':')[2] == ' 0.000000':
    line = lines[0].split(',')[0].split('/')[-1]+'\n'
    data_error +=line
    data += line

for i in range(3,m,2):
    # print (i)
    l1 = lines[i-2].split(',')[0].split(':')[2]
    l2 = lines[i].split(',')[0].split(':')[2]
    line = lines[i-1].split(',')[0].split('/')[-1]+'\n'
    # print(line)
    if l1 > l2:
        data_error += line
        data += line
    else:
        data_correct += line
        data +=line

# data_correct = sorted(data_correct)

correct_path = source_path + 'correct.txt'
error_path = source_path + 'error.txt'
with open(correct_path,'w') as w1:
    # data_correct = sorted(data_correct)
    w1.write(data_correct)
w1.close()

with open(error_path,'w') as w2:
    # data_error = sorted(data_error)
    w2.write(data_error)
w2.close()

# accuracy = []
correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open(correct_path,'r') as r:
    lines = r.readlines()
    # print(lines)
    for line in lines:
        if line.find('false_positive') > 0:
            correct[0] +=1
            # print(correct[0])
        elif line.find('traffic_sign_05') > 0:
            correct[1] +=1
        elif line.find('traffic_sign_15') > 0:
            correct[2] +=1
        elif line.find('traffic_sign_20') > 0:
            correct[3] +=1
        elif line.find('traffic_sign_30') > 0:
            correct[4] += 1
        elif line.find('traffic_sign_40') > 0:
            correct[5] += 1
        elif line.find('traffic_sign_50') > 0:
            correct[6] += 1
        elif line.find('traffic_sign_60') > 0:
            correct[7] += 1
        elif line.find('traffic_sign_65') > 0:
            correct[8] += 1
        elif line.find('traffic_sign_70') > 0:
            correct[9] += 1
        elif line.find('traffic_sign_80') > 0:
            correct[10] += 1
        elif line.find('traffic_sign_100') > 0:
            correct[11] += 1
        elif line.find('traffic_sign_110') > 0:
            correct[12] += 1
        elif line.find('traffic_sign_120') > 0:
            correct[13] += 1
        elif line.find('traffic_sign_lowest_50') > 0:
            correct[14] += 1
        elif line.find('traffic_sign_lowest_60') > 0:
            correct[15] += 1
        elif line.find('traffic_sign_lowest_70') > 0:
            correct[16] += 1
        elif line.find('traffic_sign_lowest_80') > 0:
            correct[17] += 1
        elif line.find('traffic_sign_lowest_90') > 0:
            correct[18] += 1
        elif line.find('traffic_sign_lowest_100') > 0:
            correct[19] += 1
        elif line.find('traffic_sign_lowest_110') > 0:
            correct[20] += 1
        elif line.find('traffic_sign_remove_20') > 0:
            correct[21] += 1
        elif line.find('traffic_sign_remove_30') > 0:
            correct[22] += 1
        elif line.find('traffic_sign_remove_40') > 0:
            correct[23] += 1
        elif line.find('traffic_sign_remove_60') > 0:
            correct[24] += 1
        elif line.find('traffic_sign_remove_65') > 0:
            correct[25] += 1
        elif line.find('traffic_sign_remove_80') > 0:
            correct[26] += 1
        elif line.find('traffic_sign_remove_120') > 0:
            correct[27] += 1

print(correct)


data = data.split('\n')
# print(data)
# print(data)
for d in data:
    # print(d)
    if d.find('false_positive') > 0:
        total[0] += 1
        # print(total[0])
    elif d.find('traffic_sign_05') > 0:
        total[1] += 1
    elif d.find('traffic_sign_15') > 0:
        total[2] += 1
    elif d.find('traffic_sign_20') > 0:
        total[3] += 1
    elif d.find('traffic_sign_30') > 0:
        total[4] += 1
    elif d.find('traffic_sign_40') > 0:
        total[5] += 1
    elif d.find('traffic_sign_50') > 0:
        total[6] += 1
    elif d.find('traffic_sign_60') > 0:
        total[7] += 1
    elif d.find('traffic_sign_65') > 0:
        total[8] += 1
    elif d.find('traffic_sign_70') > 0:
        total[9] += 1
    elif d.find('traffic_sign_80') > 0:
        total[10] += 1
    elif d.find('traffic_sign_100') > 0:
        total[11] += 1
    elif d.find('traffic_sign_110') > 0:
        total[12] += 1
    elif d.find('traffic_sign_120') > 0:
        total[13] += 1
    elif d.find('traffic_sign_lowest_50') > 0:
        total[14] += 1
    elif d.find('traffic_sign_lowest_60') > 0:
        total[15] += 1
    elif d.find('traffic_sign_lowest_70') > 0:
        total[16] += 1
    elif d.find('traffic_sign_lowest_80') > 0:
        total[17] += 1
    elif d.find('traffic_sign_lowest_90') > 0:
        total[18] += 1
    elif d.find('traffic_sign_lowest_100') > 0:
        total[19] += 1
    elif d.find('traffic_sign_lowest_110') > 0:
        total[20] += 1
    elif d.find('traffic_sign_remove_20') > 0:
        total[21] += 1
    elif d.find('traffic_sign_remove_30') > 0:
        total[22] += 1
    elif d.find('traffic_sign_remove_40') > 0:
        total[23] += 1
    elif d.find('traffic_sign_remove_60') > 0:
        total[24] += 1
    elif d.find('traffic_sign_remove_65') > 0:
        total[25] += 1
    elif d.find('traffic_sign_remove_80') > 0:
        total[26] += 1
    elif d.find('traffic_sign_remove_120') > 0:
        total[27] += 1

print(total)
# name_list = ['false_positive','traffic_sign_05','traffic_sign_15','traffic_sign_20','traffic_sign_30','traffic_sign_40',
#              'traffic_sign_50','traffic_sign_60','traffic_sign_65','traffic_sign_70','traffic_sign_80',
#              'traffic_sign_100','traffic_sign_110','traffic_sign_120','traffic_sign_lowest_50','traffic_sign_lowest_60',
#              'traffic_sign_lowest_70','traffic_sign_lowest_80','traffic_sign_lowest_90','traffic_sign_lowest_100',
#              'traffic_sign_lowest_110','traffic_sign_remove_20','traffic_sign_remove_30','traffic_sign_remove_40',
#              'traffic_sign_remove_60','traffic_sign_remove_65','traffic_sign_remove_80','traffic_sign_remove_120']
name_list=['false','05','15','20','30','40','50','60','65','70','80','100','110','120','l_50','l_60','l_70','l_80',
           'l_90','l_100','l_110','r_20','r_30','r_40','r_60','r_65','r_80','r_120']
num_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,28):
    if total[i]!=0:
        num_list[i] = correct[i]/total[i]
        # num_list[i] = round(num,2)
        print(num_list[i])

print(num_list)

# 定义柱状图中每个柱代表的值 并且让其居中显示 ha表示横向对齐方式 va表示纵向对齐方式
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.05,1.02*height, "%.2f" % float(height),ha='center', va='bottom')
        # plt.text(rect.get_x()+rect.get_width()/2.-0.05, 1.02*height, "%s" % float(height))


plt.figure(figsize=(15, 10))
plt.xlabel('speed_limit')
plt.ylabel('accuracy')
plt.title("valid_accuracy")
rect = plt.bar(range(len(num_list)),num_list,color='rgb',tick_label=name_list)
# plt.bar(range(len(num_list)),num_list,color='rgb')
autolabel(rect)
# plt.show()

plt.savefig("accuracy.jpg")
