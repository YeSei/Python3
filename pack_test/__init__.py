# Author:Jay
#《《《《《《模块导入详细介绍》》》》》》》
print("pack_init")
from . import bin,conf,core         #在外部使用包时使用import pack_test格式
__all__ = ['core','bin','conf']    #在外部使用包时使用from pack_test import * 格式
