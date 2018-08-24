# Author:Jay
'''
生成器函数:（特殊的迭代器）
1：编写为常规的def语句，但是使用yield语句一次返回一个结果，在每个结果之间挂起和继续它们的状态；
2：它们返回按需产生结果的一个对象，而不是构建一个结果列表。
生成器函数自动在生成值的时刻挂起并继续函数的执行
生成器是单迭代对象
'''
'''
生成器函数和常规函数之间的主要代码不同之处：
生成器yield一个值，而不是返回一个值，yield语句挂起该函数并向调用者发送回一个值，
但是，保留足够的状态以使得函数能够从它离开的地方继续
'''

import time
def consumer(name):
    print("%s准备吃包子了" % name)
    while True:
        baozi = yield
        print("包子%s来了，被%s吃了" % (baozi,name))
'''
def con(name):
    return name
n =con("jay")      #函数由括号开始调用
print(n)
c = consumer("jay")#生成器函数只能由__next__()或者内置next方法开始调用，
b1 = "肉"
c.__next__()
c.send(b1)
c.__next__()
'''

def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print("老子%s开始做包子了" % name)
    for i in range(10):
        time.sleep(1)
        print("做了一个包子，分两半")
        c1.send(i)
        c2.send(i)

producer("jay")