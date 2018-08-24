# Author:Jay

import pack_test       #先输出pack_init后输出core_init表明查找顺序
pack_test.core.main.ab_import()
pack_test.core.main.rl_import()
pack_test.core.read1.str()
'''
这种导入工具包方法较为简便，要求工具包中每个包的init.py都有from . import m1,m2,m3,...来导入当前
包中所有模块。
'''


# from pack_test.core import *
# main.ab_import()
# main.rl_import()
'''
这种导入工具包方法，导入指定工具包中的子包的init.py中列表__all__所有模块，
细化后即为绝对导入格式测试结果：
from pack_test.bin.tool import tool
tool()
'''