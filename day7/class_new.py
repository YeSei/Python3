# _*_coding:utf-8 _*_
__author__ = 'Jay'

class Foo():
    def talk(self):
        print("hello jay")

a = Foo()
print(a.__class__)
print(type(a))
print(type(Foo))

def talk(self):
    print("hello jay")

def __init__(self,name,age):
    self.name = name
    self.age = age
Foo2 = type('Foo2',(),{'talk' : talk,'__init__':__init__})  # Foo是type的一个实例
b = Foo2('jay',23)                              # b是Foo的一个实例
b.talk()

