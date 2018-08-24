# Author:Jay
#data = open("yesterday",encoding="utf-8").read()
#f = open("yesterday","r",encoding="utf-8")
# data = f.read()
# data2 = f.read()
# print(data)
# print("-------data2-------")
# f.close()

# f1 = open("yesterday2","w",encoding="utf-8")
# f1.write("我爱北京天安门")
# f1.close()

# f3 = open("yesterday2","a",encoding="utf-8")
# f3.write("\n天安门上太阳升")
# f3.close()

'''
for index,line in enumerate(f.readlines()):#先把每行生成列表，占用大量内存
    if index == 8:
        print("=====分割线=====")
        continue
    print(line.strip())
'''

'''
f = open("yesterday","r",encoding="utf-8")
for line in f:#文件迭代器，节省内存
    print(line.strip())
f.close()
'''

'''
f = open("yesterday","r",encoding="utf-8")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(10)
print(f.readline())

print(f.encoding)
'''

'''
#写入文件只能追加到文件末尾
f = open("yesterday","r+",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
f.write("=======addd=======")
print(f.readline())
'''

