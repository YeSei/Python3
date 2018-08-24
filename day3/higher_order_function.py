# Author:Jay
'''
高阶函数：
1:函数接受另一个函数名做参数
2:返回值中包含函数名
'''
def add(a,b,f):
    return f(a)+f(b)
res = add(3,-6,abs)
print(res)