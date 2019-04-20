import os

# source_path = '/home/hjm/darknet/data/lenet/test/'
source_path = '/home/hjm/traffic_valid/t_test/traffic_sign/'
dst_path = '/home/hjm/traffic_valid/t_test/version/'

list1 = os.listdir(source_path)
list2 = sorted(os.listdir(dst_path))

for l in list2:
    print(l)

for l1 in list1:
    path1 = os.path.join(source_path,l1)
    # find返回查询字符串的起始索引值
    if (l1.find('false_positive')>0):
        path2 = os.path.join(dst_path, list2[0]) + '/'
        os.system('mv '+ path1 +' '+path2)
    elif l1.find('traffic_sign_15')>0:
        path2 = os.path.join(dst_path,list2[5]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_20')>0:
        path2 = os.path.join(dst_path,list2[6]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_30')>0:
        path2 = os.path.join(dst_path,list2[7]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_40')>0:
        path2 = os.path.join(dst_path,list2[8]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_50')>0:
        path2 = os.path.join(dst_path,list2[9]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_60')>0:
        path2 = os.path.join(dst_path,list2[10]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_70')>0:
        path2 = os.path.join(dst_path,list2[12]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_80')>0:
        path2 = os.path.join(dst_path,list2[13]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_100')>0:
        path2 = os.path.join(dst_path,list2[2]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_120')>0:
        path2 = os.path.join(dst_path,list2[4]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_lowest_60')>0:
        path2 = os.path.join(dst_path,list2[17]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_lowest_80')>0:
        path2 = os.path.join(dst_path,list2[19]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_lowest_100')>0:
        path2 = os.path.join(dst_path,list2[14]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
    elif l1.find('traffic_sign_remove_80')>0:
        path2 = os.path.join(dst_path,list2[27]) + '/'
        os.system('mv ' + path1 + ' ' + path2)
