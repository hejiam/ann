import os

if __name__ == '__main__':
    source_floder = '/home/hjm/test/'
    t_floder = '/home/hjm/t/'
    file_list = os.listdir(source_floder)
    # print(file_list)
    file_list = sorted(file_list)
    count = 1
    for file in file_list:
        file_path = os.path.join(source_floder,file)
        #print(file_path)
        obj_list = os.listdir(file_path)
        obj_list = sorted(obj_list)
        #print(obj_list)
        for obj in obj_list:
            oldDir = file_path + '/' + obj
            print(oldDir)
            newDir = t_floder+'%05d' % count +'.jpg'
            print(newDir)
            # print(newDir)
            # 重命名文件时需要输入路径
            os.rename(oldDir, newDir)
            # print(file)
            count += 1