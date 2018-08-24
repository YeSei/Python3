# Author:Jay
#斐波拉契函数
'''
生成器只有在调用时才会生成相应的数据
只记录当前位置
只有一个__next__()方法。next（）

'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b #t=(b,a+b) , (a,b)=t
        n= n + 1
    return 'done'
f = fib(10)
print(f)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())