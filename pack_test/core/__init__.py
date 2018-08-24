# Author:Jay
print("core_init")
from . import main,read1,read2          #在外部使用import pack_test格式时
def func():
    print("core.init.py")
'''不管是哪种方式，只要是第一次导入包或者是包的任何其他部分，都会依次执行包下的__init__.py文件
(我们可以在每个包的文件内都打印一行内容来验证一下)，这个文件可以为空，但是也可以存放一些初始化
包的代码。
'''
__all__ = ['x','func','main','read1','read2'] #在外部使用from pack_test.core import * 格式时
'''
当使用from xx.core import*形式时,则导入__all__列表中的子模块和子包导入到当前作用域中来，
注意string不在__all__中则依然不能导入
'''