# Author:Jay

'''
info = {'name':'jay','age':23}
f = open("text.txt","r")
f.write(str(info))
f.close()

L = open("text.txt","r")
data = eval( L.read() )
L.close()
print(data)
'''

import json
info = {'name':'jay','age':23}
f = open("text.txt","w")
f.write(json.dumps(info))  #json.dumps实现序列化
f.close()

l = open("text.txt","r")
data = json.loads(l.read())#json.loads实现反序列化
#json操作对象必须是字符串，字节或字节数组等，故在loads中要使用read读出字符串
'''
附：文件中read，readline和readlines的区别
read() ：每次读取整个文件，它通常将读取整个文件内容放到一个字符串变量中。
readline():每次读取文件的一行，通常也是读取到的一行内容放到一个字符串变量中，返回str类型。
readlines()：每次按行读取整个文件内容，将读取到的内容放到一个列表中，返回list类型。
'''
print(data)

'''
def test():pass
info2 = {'name':'jay','age':23,'func':test} #test为函数内存地址
f = open("text.txt","w")
f.write(json.dumps(info2))  #出错，json不能序列化此函数内存地址。
                            #json只能用于简单类型(字符串，字符，字符数组)之间转换
f.close()
'''

import pickle
info2 = {'name':'yesei','age':23}
f = open("text2.txt","wb")
#f.write(pickle.dumps(info2))  #pickle实现序列化,pickle创建一个bytes字符串对象将python对象保存为二进制形式。
pickle.dump(info2,f)#等同于上句,区别在于dump需接受文件名作为参数
f.close()

f = open("text2.txt","rb")
print(pickle.load(f))  #这里也可写成pickle.loads(f.read()),s结尾方法处理一个字符串对象，不能迭代处理
f.close()

'''
注：以s结尾和无s结尾方法的区别：
以s结尾的方法作用于处理一个（整个）字符串对象（不能处理可迭代对象)或生成一个字符串对象
无s结尾的方法可作用于处理一个可迭代对象，但可能生成单个字符串对象如read()，
也可能迭代生成多个字符串对象如readline()
'''

'''
#pickle是python中特有的序列化python对象方法，可处理复杂的python对象
def test():pass
info3 = {'name':'yesei','age':23,'func':test}
f = open("text3.txt","wb")
f.write(pickle.dumps(info3))  
f.close()

f = open("text3.txt","rb")
print(pickle.load(f))  #这里也可写成pickle.loads(f.read()),s结尾方法处理一个字符串对象，不能迭代处理
f.close()
'''