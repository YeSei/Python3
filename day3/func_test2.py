# Author:Jay
def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 0

def test3():
    print('in the test3')
    return 1,'hello',['jay','yesei'],{'name':'jay'}#多个返回值以元组形式返回

x = test1()
y = test2()
z = test3()
print(x,'\n',y,'\n',z,'\n')