# Author:Jay
import day5.module_test
'''
导入优化:
当多次调用某模块函数时可使用from语句代替import导入优化
from day5.module_test import module
之后直接使用module（）即可调用
'''
def temp1():
    day5.module_test.module()
    print("temp1")

def temp2():
    day5.module_test.module()
    print("temp2")