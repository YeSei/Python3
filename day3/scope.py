# Author:Jay
'''
作用域法则：函数定义本地作用域，模块定义全局作用域
1：全局作用域的作用范围仅限于单个文件
2：每次对函数的调用都创建了一个新的本地作用域
3：赋值的变量名除非声明为全局变量或非本地变量，否则均为本地变量

LEGB原则：
1：函数中使用变量名查找顺序：L本地作用域，E上层结构中def或lambda的本地作用域，G全局作用域，B内置作用域；
2：当函数中给一个变量名赋值时总是创建或改变本地作用域的变量名，除非已经在那个函数中过声明为全局变量；
3：当在函数之外给一个变量名赋值时，本地作用域与全局作用域是相同的。
'''
#Global scope
x = 99
def func1(y):
    # local scope
    z = x+y
    return z
print(func1(1))

'''
内置作用域：是通过一个名为__builtin__的标准库模块来实现,其中预定义的变量名
内置作用域的使用防止由LEGB原则引起的覆盖内置函数导致的BUG
'''
import builtins
print(builtins.zip())
print(dir(builtins))

'''
global语句使用：
1：全局变量是位于模块文件内部的顶层的变量名
2：全局变量如果是在函数内被赋值的话，必须经过声明
3：全局变量在函数内部不经过声明也可以使用
'''
y = 88
def func2():
    global y
    y =99
func2()
print(y)
'''
注：
滥用全局变量增加函数之间耦合性，使得程序变得难以理解和使用，
在实际使用中应最小化全局变量，减少全局变量的使用
'''

'''
nonlocal语句:意味着完全略过我的本地作用域
nonlocal应用于一个嵌套的函数的作用域中的一个名称，而不是所有def之外的全局作用域；
并且声明nonlocal时，它必须已经存在于该嵌套函数中。
global使得作用域的查找从嵌套的模块的作用域开始，如果名称不存在该模块则继续查找内置作用域，
nonlocal限制作用域查找只是嵌套的def，作用域查找不会继续到全局或内置作用域
'''
def tester(start):
    state = start
    def nested(label):
        nonlocal state #若无此句则下面state += 1报错
        print(label,state)
        state += 1
    return nested
F = tester(0)
F('spam')
F('ham')
#注：nonlocal允许在内存中保持可变状态的多个副本，

#嵌套作用域：有时也叫静态嵌套作用域
def f1():
    x = 88
    def f2():
        print(x)
    return f2
action = f1()
action()
'''
这段代码中，命名f2的函数调用动作的运行是在f1运行后发生的，
f2记住了f1中嵌套的作用域中的x，尽管f1已经不处于激活状态
'''
