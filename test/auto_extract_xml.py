import os

path='/home/hjm/traffic_valid/Annotation0'
for maindir, subdir, filenames in os.walk(path):
    filenames = sorted(filenames)
    for filename in filenames:
        print(filename)
        os.system('python extract_xml.py -o %s' % filename)
