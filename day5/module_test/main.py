# Author:Jay
import module_jay #python3一般只支持绝对导入和相对导入，这种写法不安全。
#查找路径：当前文件目录-》工作主目录-》sys.path其他
#导入多个模块以逗号分隔。
module_jay.hello()
print(module_jay.name)

import sys
print(sys.path)
'''
注1：
from module_jay import *

def hello():
   pass

导入的hello（）函数无效。
解决方法：使用as语句
from modile_jay import hello as upper_hello
使用upper_hello（）代替上层hello（）函数，且使上层hello（）无效；不影响本层hello（）。
'''

