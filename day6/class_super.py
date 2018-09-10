# Jay
class A(object):
    def __init__(self):
        print("A")

class B(object):
    def __init__(self):
        print("B")

class C(B,A):
    def __init__(self):
        super(C,self).__init__()

c = C()

#注意！！！使用super只会匹配上级一个init函数，匹配完成过后，其他父类函数不做考虑。