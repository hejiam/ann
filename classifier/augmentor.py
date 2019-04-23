# import Augmentor
# # 保存图片的路径及增强后所有图片的存储路径 会存放在该路径下的output文件夹下
# p = Augmentor.Pipeline("/home/hjm/images")
# # 对图像进行旋转操作 参数包括旋转的概率和左右旋转的最大角度
# p.rotate(probability=0.7,max_left_rotation=10,max_right_rotation=10)
# # 最后生成图片的个数
# p.sample(30)


import os
import Augmentor
# path_to_data = "/home/hjm/lenet_train/image_old/false-positive/"

# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_120/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_80/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_65/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_60/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_40/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_30/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_remove_20/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_110/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_100/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_90/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_80/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_70/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_60/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_lowest_50/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_110/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_65/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_15/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_05/"


# path_to_data = "/home/hjm/images/2/o2/traffic_sign_120/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_100/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_60/"
#
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_40/"
# path_to_data = "/home/hjm/images/2/o2/traffic_sign_20/"
#
# path_to_data = '/home/hjm/images/2/o2/false_positive/'
# path_to_data = "/home/hjm/images"

path_to_data = '/home/hjm/images/3/train/traffic_sign_20/'
# src_path = '/home/hjm/images/3/train/'
# list = os.listdir(src_path)

# for l in list:
# path_to_data = os.path.join(src_path,l) + '/'
# create a pipeline
p = Augmentor.Pipeline(path_to_data)

# 对图像进行旋转 可设置最大旋转角度和最小旋转角度
# p.rotate(probability=0.5,max_right_rotation=20,max_left_rotation=25)
# p.rotate_without_crop(probability=0.5,max_left_rotation=20,max_right_rotation=20)

# 转换图像像素值强度从0-255变化
# p.greyscale(probability=0.5)
# 随机改变像素亮度
p.random_brightness(probability=0.5,min_factor=0.5,max_factor=1.5)
# 改变图像的饱和度
# p.random_color(probability=0.5, min_factor=0.5,max_factor=2)
# 随机改变图像对比度
p.random_contrast(probability=0.5,min_factor=0.5,max_factor=1.5)
# 对图像的大小进行等比例变换 scale_factor必须大于1
p.scale(probability=0.8, scale_factor=2)
# if l.find('sign_05') >0:
#     p.sample(2000)
# elif l.find('sign_15')>0:
#     p.sample(2000)
# elif l.find('sign_30') >0:
#     p.sample(1740)
# elif l.find('sign_50') >0:
#     p.sample(1800)
# elif l.find('sign_70') >0:
#     p.sample(1500)
# elif l.find('sign_100') >0:
#     p.sample(1400)
# elif l.find('sign_110') >0:
#     p.sample(1850)
# elif l.find('sign_120') >0:
#     p.sample(1400)
p.sample(1550)


# 对图像放大后进行随机剪切
# p.zoom_random(probability=1, percentage_area=0.2)
# p.zoom(probability=0.5, min_factor=1.2, max_factor=2)

# perspective skewing
# 上下左右的透视形变
# p.skew_tilt(probability=0.5,magnitude=1)
# p.skew_tilt(probability=1,magnitude=1)
#  向四个角透视形变
# p.skew_corner(probability=0.5,magnitude=1)
# 进行所有角度的随机形变
# p.skew(probability=1,magnitude=0.2)

# 将原图像裁剪为固定尺寸大小 centre表示是否从中心裁剪
# p.crop_by_size(probability=1, width=100, height=100,centre = True)
# 将原图像中的80%区域裁剪为新图像 randomise_percentage_area表示是否随机裁剪部位
# p.crop_centre(probability=1, percentage_area=0.8)
# p.crop_centre(probability=0.5, percentage_area=0.8, randomise_percentage_area=True)
#
# p.crop_random(probability=1, percentage_area=0.8)