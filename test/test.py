import os

# test_floder = '/home/hjm/t/'
test_floder = '/home/hjm/traffic_valid/valid/valid/'
# source_floder = '/home/anngic/dataset/data_anngic/traffic_sign/ts/'
source_floder = '/home/anngic/dataset/data_anngic/traffic_sign/t/'
# txt_floder = '/home/hjm/test.txt'
txt_floder = '/home/hjm/traffic_valid/valid/valid.txt'

file_list = os.listdir(test_floder)
file_list = sorted(file_list)
file_data = ""

w = open(txt_floder,'w')

for file in file_list:
    file_data +=source_floder+file+'\n'
w.write(file_data)

w.close()
