# _*_coding:utf-8 _*_
__author__ = 'Jay'

# 使用type实现类的建立与继承：

Dog = type('Dog',(),{'name':'二哈','age':1})
print(Dog)
help(Dog)

DogChild = type('DogChild', (Dog,),{})
print(DogChild)
print(DogChild.name)

# 使用type实现带有方法的类：
#普通方法
def test(self):
    print("test")

#静态方法
@staticmethod
def static_test():
    print("static_test")

#类方法
@classmethod
def class_test(cls):
    print("class_test")

Test = type('Test',(),{'name':'name','test':test,'static_test':static_test,'class_test':class_test})
print(Test)

test = Test()
test.test()
test.static_test()
test.class_test()