import os
import shutil

if __name__ == "__main__":
    # 视频存储地址
    source_floder = '/home/hjm/test/'
    # 执行命令行后图片的地址
    test_floder = '/home/hjm/traffic_valid/'
    # 将图片统一处理的文件地址
    valid_floder = '/home/hjm/t/'
    # 视频名称
    file_list = os.listdir(source_floder)

    for obj in file_list:
        # file=""
        # 存储视频的路径
        obj_path = os.path.join(source_floder,obj)
        # print(obj_path)
        # 视频中每张图像的名称
        obj_list = os.listdir(obj_path)
        # print(obj_list)
        for img in obj_list:
            # 图像存储路径
            img_path = obj_path+'/'+ img
            # 执行命令行
            os.system('./darknet detector test cfg/traffic_sign_1.data cfg/traffic_sign_1_test.cfg '
                      +' weights/traffic_sign_1/traffic_sign_1_18000.weights ' +img_path)
            # os.system('mkdir '+test_floder+'a.jpg')
            # 对存储的图像进行重命名
            # oldDir = test_floder + 'a.jpg'
            oldDir = test_floder + 'prediction.jpg'
            newDir = test_floder + img
            # print(newDir)
            os.rename(oldDir, newDir)
            # 将图像移动到存储文件夹中valid_floder,并且按照视频文件夹进行保存
            # newDir1 = valid_floder
            # shutil.move(newDir, newDir1)
            newDir1 = os.path.join(valid_floder,obj)+'/'
            # print(newDir1)
            shutil.move(newDir, newDir1)


