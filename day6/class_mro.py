# Jay
#参考https://blog.csdn.net/new_abc/article/details/47904595
class A(object):
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super(B,self).__init__()
        print("B")


class C(A, B):
    def __init__(self):
        super(C,self).__init__()
        print("C")

if __name__ == '__main__':
    print(C.__mro__)
    C_child = C()

'''
__mro__给出了method resolution order，即解析方法调用的顺序。凡是基-派生类型的多继承，必须由下往上顺序书写。
此处class C(A, B)就会出现MRO错误，必须写成class C(B, A)顺序形式，不是基-派生类型的多继承则不用按顺序书写。

注意！！！python3严格按照广度优先顺序搜索继承。如果有class M(Q,W),且W在Q上层（两层以上能看出差别），则从最底层广度遍历到Q，在遍历Q的
上一层，依次按层数遍历到W。
'''