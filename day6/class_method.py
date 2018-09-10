# Jay
class A(object):
    def __init__(self, name):
        self.name = name
        self.__x = None

    def foo(self,x):
        print("%s excute %s" % (self.name,x))  #普通方法默认传入第一个参数为类的实例对象

    @classmethod
    def class__foo(cls,x):
        print("%s excute %s" % (cls,x))  # 类方法默认传入的第一个参数为类对象

    @staticmethod
    def static__foo(self, x):
        print("%s excute %s" % (self.name, x))  # 静态方法与普通函数一样，但是它是嵌入类内部的函数，使用类或类实例调用。

    @property
    def pro_foo(self):
        print("%s excute %s" % (self.name, self.__x))

    @pro_foo.setter
    def pro_foo(self,x):
        self.__x = x

class B(object):
    def __init__(self,name):
        self.name = name
a = A("dyj")
# 普通方法调用方式：
a.foo(1)
A.foo(a,1)

# 类方法调用方式:
a.class__foo(1)
A.class__foo(1)

# 类的静态方法调用方式：
A.static__foo(a, 1)
a.static__foo(a, 1)
b = B("dyj2")
A.static__foo(b,1)

#类的属性方法调用：
a.pro_foo
a.pro_foo = 1
a.pro_foo

'''
Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.
普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。
@staticmethod修饰的方法定义与普通函数是一样的。self和cls的区别不是强制的.
另外，属性方法:将方法自动保存为属性动作，使用@相应方法名.setter可以为属性方法接受传入值。
'''