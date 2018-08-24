# Author:Jay
print(all([0,1,2]))
print(any([1,2,3]))

a = ascii([1,2])
print(type(a))#把里面的值转换成字符串

bin(10)#把数字转成二进制

a = bytes("abcde",encoding="utf-8")
print(a.capitalize(),a)
b = bytearray("abcde",encoding="utf-8")#将字符串变成字符数组可以按索引修改
print( b[1] )
b[1] = 100
print(b)

def qw():pass
print(callable(qw))#判断是否可以调用，即加括号后调用

print(chr(97))#chr()接受数字，返回数字在ascll码中的值

code1 = "for i in range(10):print(i)"
code2 = "3*5+10"
c1 = compile(code1,'','exec')
c2 = compile(code2,'','eval')
'''compile将一个字符串编译为字节代码,
参数分别为字符串对象，文件名（不可省可空），编译代码的种类可为exec，exal，single，
如果是exec类型，表示这是一个序列语句，可以进行运行；
如果是eval类型，表示这是一个单一的表达式语句，可以用来计算相应的值出来；
如果是single类型，表示这是一个单一语句，采用交互模式执行，
在这种情况下，如果是一个表达式，一般会输出结果，而不是打印为None输出。
'''
print(c1,c2)
exec(c1)
print(eval(c2))

d = []
print(dir(d))#打印dir，显示某对象中的所有属性及方法
help(d)#显示某对象中属性的值及方法的使用说明

print(divmod(5,2))#返回一个商和余数的元组
print(divmod(5,3))

import sys
f = lambda x:sys.stdout.write(str(x)+'\n')
'''
匿名函数lambda是一个表达式而不是一个语句，
lambda的主体必须是单个表达式，而不是一些代码块
模块》》语句》》函数》》表达式
'''
for i in range(10):
    f(i)

res = filter(lambda n:n>5,range(10))#过滤器函数
for i in res:
    print(i)

we = map(lambda n:n*2,range(10))#对集合中每个元素使用前面的函数
for i in we:
    print(i)

import functools
qa = functools.reduce(lambda x,y:x+y,range(10))
'''
reduce位于functools模块中，它接受一个迭代器来处理但是它本身不是一个迭代器，
它返回一个单个的结果，它每一步传递当前的一对值的计算结果和列表中下一个元素。
'''
print(qa)

e = frozenset([1,2,3,54])#将集合的修改方法pop，add等全部去掉
print(globals())#返回本模块中所有的全局变量：值的字典

print(round(1.33455,2))#四舍五入，第二个参数指定保留位数

f = {6:2,8:0,9:10,11:24,1:4,-3:2,14:16}
print(f)
print(sorted(f.items()))
print(sorted(f.items(),key=lambda x:x[1]))

g = [1,2,3,]
h = ['a','b','c','d']
for i in zip(g,h):
    print(i)