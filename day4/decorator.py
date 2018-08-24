# Author:Jay
'''
装饰器：本质上是函数，为其他函数或类提供附加功能
原则：
1：不能修改被装饰函数的源代码
2：不能修改被装饰函数的调用方式
'''
import time
def timer(func):
    def warpper(*args,**kargs):  #加入可变参数使其更为通用
        start_time = time.time()
        func(*args,**kargs)      #解包参数
        stop_time = time.time()
        print('the func run time is %s'%(stop_time - start_time))
    return  warpper
'''
实现装饰器知识储备：
1：函数即变量，加（）既可执行
2：高阶函数
3：嵌套函数
高阶函数+嵌套函数 = 装饰器
'''

@timer
def test1():
    time.sleep(3)
    print('in the test1')

@timer
def test2(name,age):
    print('name:',name,'age:',age)

test1()
test2('jay',23)