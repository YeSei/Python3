# Author:Jay
f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday.bak","w",encoding="utf-8")

for line in  f:
    if "天安门上太阳升" in line:
        line = line.replace("天安门上太阳升","哈哈哈哈哈哈哈")
    f_new.write(line)
f.close()
f_new.close()