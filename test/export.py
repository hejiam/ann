f1 = open("val.txt")
f2 = open("val_flag.txt", "w")

# line = f1.readline()
# print(line)
# print(f1.readline())
# print(f1.readline())
for line in f1.readlines():
    if line[7]=='h':
        f2.write(line)
        print(line)
        print("ok")

f1.close()

with open('0095999.txt','r') as r:
    lines = r.readlines()
with open('0095999.txt', 'w') as w:
    for l in lines:
        if l[0] == '3':
            w.write(l)