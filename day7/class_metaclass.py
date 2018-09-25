# _*_coding:utf-8 _*_
__author__ = 'Jay'

#元类的主要目的就是为了当创建类时能够自动地改变类。通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类
'''
假想一个例子，你决定在你的模块里所有的类的属性都应该是大写形式。
有好几种方法可以办到，但其中一种就是通过在模块级别设定metaclass。采用这种方法，这个模块中的所有类都会通过这个元类来创建，
我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。幸运的是，metaclass实际上可以被任意调用，
它并不需要是一个正式的类。所以，我们这里就先以一个简单的函数作为例子开始。
'''
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        #遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)

#python2的用法
#class Foo(object):
#    __metaclass__ = UpperAttrMetaClass
#    bar = 'bip'

# python3的用法
class Foo(object, metaclass = UpperAttrMetaClass):
     bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)