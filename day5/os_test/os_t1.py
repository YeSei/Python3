import os
a = os.getcwd() #当前路径
print(a)
os.chdir("/Users/dengyangjie/PycharmProjects/oldboy") #改变当前工作目录
a = os.getcwd()
print(a)
os.mkdir("/Users/dengyangjie/PycharmProjects/oldboytest")
print(os.listdir("/Users/dengyangjie/PycharmProjects/")) #显示当前目录下内容
os.removedirs("/Users/dengyangjie/PycharmProjects/oldboytest")

print(os.sep)  #输出os平台路径分隔符，常用于跨平台。
print(os.linesep)
print(os.environ)
print(os.pathsep)

print(os.path.abspath(__file__))  #输出当前绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  #输出当前文件的父级目录

print(os.path.split("/Users/dengyangjie/Documents/GitHub/python3/day5/os_test/os_t1.p")) #分割path为目录和文件名
print(os.path.split(os.path.abspath(__file__)))
