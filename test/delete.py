import os

# file = open('traffic_train.txt','r')
# file2 = open('t_test.txt','w')
#
# count = 0
# for f in os.listdir('/home/hjm/darknet/traffic_sign/l_test'):
#     f1 = f[:-4]
#     for line in file.readlines():
#         if line.find(f1)>0:
#             file2.write(line)
#             print('success')
#         count += 1
# print(count)

filedir = "/home/hjm/darknet/traffic/"
count = 0
# 定义file_data为列表
file_data = []
file_data1 = []
count_1 = 0
# 将路径定义为一个变量
jpg_path="/home/anngic/dataset/data_anngic/traffic_sign/JPEGImages/"

for file in os.listdir(filedir+"labels"):
    #print(file)
    #print(os.path.getsize(filedir+"labels/"+file))
    # 如果文档大小为空
    # if os.path.getsize(filedir+"labels/"+file) == 0:
    #     print(file)
    #     os.remove(filedir+"labels/"+file)
    #     os.remove(filedir + "JPEGImages/"+file[:-4]+".jpg")
    #     print("success")
    #     count+=1
    file_data.append(jpg_path+file[:-4]+".jpg\n")
    # file_data.append(jpg_path+file.strip('.txt'+'.jpg\n'))
    file_data1.append(file[:-4]+'\n')

    # with open(file, 'r') as r:
    #     for line in file:
    #
    # with open(file,'w') as w:
    #     for l in lines:
    #         if l[0] == '3':
    #             w.write(l)
file_data.sort()
file_data1.sort()
with open("/home/hjm/darknet/traffic/test-train.txt","w") as w:
    for i in range(0,len(file_data)):
        w.write(file_data[i])
with open("/home/hjm/darknet/traffic/test.txt","w") as w:
    for i in range(0,len(file_data1)):
        w.write(file_data1[i])
print(count)





