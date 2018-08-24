# Author:Jay
'''
python3按照如下顺序进行参数匹配：
1：位置参数
2：关键字参数：
3：非关键字可变参数分配进入*names中
4：关键字可变参数分配进入**name中
5：用默认值分配给头部未得到分配的参数
'''
def test(x,y):
    print(x)
    print(y)
#按位置分配参数
test(1,2)

#按关键字分配参数，此处x,y对应函数参数列表中的x，y,且与位置无关.
test(y = 1,x = 2)

#test(x=1,2)函数出错，原因见文档注释，若有多种赋值方式混用则先按1：位置参数，再按2：关键字参数，赋值.
test(1,y=2)

#默认值参数
def test2(x,y=2):
    print(x)
    print(y)
test2(3)
test2(3,4)#默认值参数优先级低于位置和关键字参数.

#可变任意参数:非关键字存入*names和关键字存入**names.
def test3(x,y,*pargs,**kargs):#names以元组形式收集后续可变参数.
    print(x)
    print(y)
    print(pargs)
    print(kargs)
test3(1,2,3,4,5,6,a = 7,b = 8)

#解包参数：再函数调用时以*号将元组，列表解包为单个非关键字参数，以**将字典解析为单个关键字参数.
pargs = (1,2,3,4,8)
kargs = {'f1':9,'f2':10}
test3(*pargs,**kargs)

#keyword_only参数：位于*names之后，**，并且只按照关键字传递，可取默认值.
def test4(x,y,*pargs,z=4,**kargs):
    print(x)
    print(y)
    print(pargs)
    print(z)
    print(kargs)
#test4(0,y=1,2,3,4,z=5,a=10,b=11) #关键字参数传递不能位于*names位置参数之前.
test4(0,1,2,3,z=9,a=10,b=11)#keyword_only参数常作为附加配置信息传给函数.

#keyword_only参数还可使用一个*字符来表示一个函数不会接受一个变量长度参数，且期待后续参数作为关键字传递.
def test5(x,*,y=2,z=3):
    print(x,y,z)
test5(1,z=4,y=5)

'''
注：
在函数定义中 names = value 形式为指定默认值；
在函数调用中 names = value 形式为关键字传递。
'''