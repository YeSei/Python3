# Author:Jay
'''
函数的使用目的：
1：最大化代码重用和最小化代码冗余
2：流程的分解
'''
def log():
    with open('a.txt','a') as f:
        f.write('end action\n')

def test1():
    print('in the test1')
    log()

def test2():
    print('in the test2')
    log()

def test3():
    print('in the test3')
    log()
test1()
test2()
test3()