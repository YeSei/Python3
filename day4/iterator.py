# Author:Jay
'''
*迭代工具：
for循环，列表解析，in成员关系测试以及map内置函数等

*可迭代对象：
如果对象是实际保存的序列，或者可以在“迭代工具”环境中一次产生一个结果的对象
就看作是可迭代的。可迭代对象包括实际序列和按照需求而计算的虚拟序列。

*迭代协议（迭代器）：
1：有__next__()方法的对象会前进到下一个结果；
2：而在一系列结果的末尾时，则会引发StopiIteration.

单个迭代器/多个迭代器：
1:如列表，字典，range等是可迭代对象但不是自身的迭代器，需要调用iter来启动迭代，并用
__next__()或内置next()方法调用，这样的对象支持多次打开迭代器，；
如map，zip，filter等自身的迭代器直接使用__next__()或内置next()即可调用，但只遍历一次有效，。
'''
it = [1,2,3,4,5,6]
for x in it:
    print(x)
#next(it)出错-> 列表为可迭代对象但不是迭代器,需要iter启用
m1 = iter(it)
m2 = iter(it)
print(next(m1))
print(next(m1))
print(next(m2))   #生成多个迭代器

z = zip((1,2,3),(10,11,12,13))
l1 = iter(z)
l2 = iter(z)
print(next(l1))
print(next(l1))
print(next(l2))   #只生成并共用一个迭代器