# Author:Jay
with open("yesterday2","r",encoding="utf-8") as f,\
        open("yesterday","r",encoding="utf-8") as f2:
    for line in f:
        print(line.rstrip())
    for line2 in f2:
        print(line2.rstrip())