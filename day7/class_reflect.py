# _*_coding:utf-8 _*_
__author__ = 'Jay'

class dog():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating..." % self.name)

def bulk(self):
    print("%s is bark..."%self.name)

d = dog("qwe")
choice = input(">>:").strip()

print(hasattr(d,choice))  # 判断对象obj是否有对应的name字符串方法或属性！

#print(getattr(d,choice))  # 按照输入来调用相应方法。
#getattr(d,choice)()


if hasattr(d,choice):
    func = getattr(d,choice)
    func()
else:
    setattr(d,choice,bulk)  # setattr(x,'y',z)等价于:d.y = z
    func = getattr(d, choice)
    func(d)
