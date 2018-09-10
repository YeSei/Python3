# Jay


class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s : wang wang wang!! " % self.name)


d1 = Dog("w1")
d2 = Dog("w2")
d3 = Dog("w3")
d4 = Dog("w4")

d1.bulk()
d2.bulk()
d3.bulk()
d4.bulk()

class super(object):   # 抽象超类，也就是类的部分行为默认是由其子类所提供的。
    def action(self):
        print("super")
        self.action()   # 抽象超类的action（）功能由子类实现。

class pro(super):
    def action(self):
        print("pro")

x = pro()
x.action()
super.action(x)
super.action(pro())
