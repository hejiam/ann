import os
import shutil

if __name__ == "__main__":
    #  需要读取的图片的地址
    source_floder ='/home/hjm/t1/'
    # command命令后图像保存的地址
    test_floder = '/home/hjm/traffic_valid/'
    # 将图像从保存的地址中统一存储到文件夹的地址
    t_floder = '/home/hjm/t2/'
    # 将文件夹下的图片名字统一存储到file_listz中
    file_list=os.listdir(source_floder)
    file_list = sorted(file_list)
    # 遍历file_list 每读取一张图片 便进行一次command操作
    for file in file_list:
        # 创建图片路径以便后续命令行可以使用
        file_path = os.path.join(source_floder, file)
        # 输出图片路径验证是否正确
        # print(file_path)
        # 运行命令行在test_floder下创建文件夹
        # os.system('mkdir '+test_floder+'a')
        os.system('./darknet detector test cfg/traffic_sign_1.data cfg/traffic_sign_1_test.cfg '
                  + ' weights/traffic_sign_1/traffic_sign_1_18000.weights ' + file_path)
        # os.system('touch a.txt')
        # os.system('touch a.txt')
        # 将test_floder中的文件重命名并进行移动
        oldDir = test_floder + 'a'
        newDir = t_floder + file
        os.rename(oldDir,newDir)
        # 将文件移动到存储文件夹中t_floder
        # newDir1 = t_floder
        # shutil.move(newDir,newDir1)