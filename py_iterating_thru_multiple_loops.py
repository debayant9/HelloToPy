from datetime import datetime

stud = ["debayan","krittika","pratiti"]
age = [29,25,31]
val = zip(stud,age)
ls = list(zip(stud,age))
ts = dict(zip(stud,age))
print(ts)
print(ls)
for i,b in zip(stud,age):
    print("%s is %s" % (i,b))

#unzipping
for i in zip(*val):
    print(i)

with open("upo.txt",'w') as hu:
    hu.write("something")

time = datetime.now().strftime("%Y-%m-%d")
filename = str(time + ".txt")
with open(filename, 'w') as po:
    for file in ["file1.txt", "file2.txt", "file3.txt"]:
        txt = open(file,'r+')
        po.write(txt.read() + '\n')
