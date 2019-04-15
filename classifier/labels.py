import os


# labels_path = '/home/hjm/traffic_valid/'
labels_path = input('labels_path: ')
# transform_path = '/home/hjm/traffic_valid/'
transform_path = input('transform_path: ')

data = ''

with open(labels_path, 'r') as r:
# with open(file1_path, 'r') as r:
    lines = r.readlines()
    for line in lines:
        line = line.split("/")  # ['00001_235.jpg','u_80\n']
        # print(line)
        name = line[0].split("_")[0]
        # print(name)
        labels = line[1].split("_")
        print(labels)
        if labels[0] == 'u':
            labels = name + '_traffic_sign_'+labels[1]
            # print(labels)
        elif labels[0] == 'r':
            labels = name + '_traffic_sign_remove_'+labels[1]
        elif labels[0] == 'l':
            labels = name + '_traffic_sign_lowest_'+labels[1]
        if labels[0] == 'f\n':
            labels = name + '_false_positive\n'
        data += labels
        # print(labels)
# print(data)
r.close()

with open(transform_path, 'w') as w:
    w.write(data)
w.close()

rename_path = input('rename_path: ')
# rename_path = '/home/hjm/traffic_valid/test/'
list = sorted(os.listdir(rename_path))

with open(transform_path, 'r') as r:
    lines = r.readlines()
    for l in list:
        # src = os.path.join(file3_path, l)
        l1 = l.split('_')
        for line in lines:
            l2 = line.split('_')
            if l1[0] == l2[0]:
                src = os.path.join(rename_path,l)
                dst = rename_path + line + '.jpg'
                os.rename(src, dst)
r.close()

