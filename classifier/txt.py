import os

file_path = '/home/hjm/traffic_valid/t_test/traffic_sign/'
file1_path = '/home/hjm/traffic_valid/traffic_sign.txt'

list = os.listdir(file_path)
list = sorted(list)

with open(file1_path,'a') as f:
    for l in list:
        l = l+'\n'
        f.write(l)
