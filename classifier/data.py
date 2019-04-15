import os

source_path = '/home/hjm/traffic_valid/valid/t_sign/'
# source_path = '/home/hjm/darknet/data/lenet/'

list = os.listdir(source_path)
list = sorted(list)
print(list)

i = 0
for l in list:
    file_path = os.path.join(source_path,l)+'/'
    file_list = os.listdir(file_path)
    for f in file_list:
        # print(os.path.splitext(f)[1])
        #  os.path.splitext()分离文件名和扩展名 返回值为文件名与扩展名
        if os.path.splitext(f)[1] == '.jpg':
            src = file_path + f
            # dst = file_path + '%d'%i
            dst = file_path + '%d'%i + '_' + l + '.jpg'
            # dst = dst + '_' + l + '.jpg'
            os.rename(src, dst)
        else:
            src = file_path + f
            # dst = file_path + '%d'%i
            dst = file_path + '%d'%i + '_' + l + '.png'
            # dst = dst + '_' + l + '.jpg'
            os.rename(src, dst)
        i += 1
