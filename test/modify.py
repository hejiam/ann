# import re
# import os
#
# count=0
# # 将.py文件尽量放到处理文档的统一根目录下
# for f in os.listdir('/home/hjm/darknet/traffic/labels'):
#     print(f)
#     if f.find('.txt') > -1:
#         file_data = ""
#         with open(f,'r') as r:
#             for line in r.readlines():
#                 # if line[0]=='3':
#                 line.replace(line[0],'0')
#                 file_data+=line
#         with open(f,'w') as w:
#             w.write(file_data)
#             print("success")
#             count+=1
# print(count)
file_data = ""

with open('1.txt', 'r') as r:
    for line in r.readlines():
        # if line[0]=='3':
        # line = line.lstrip('3 ')
        s=line[0]
        line = line.replace(s,'0')
        file_data+=line
        print(line)
        # print(line)
        # file_data +='0 '+line
        # print(file_data)

with open('0.txt','w') as w:
        w.write(file_data)
        print("success")
        #count+=1