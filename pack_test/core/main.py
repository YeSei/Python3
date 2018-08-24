# Author:Jay
from pack_test.bin.atm import test#凡是导入时带点的，点的左边一定是一个包
def ab_import():                 #采用绝对导入，可以直接运行。
    test()
    print("绝对导入结束")
'''
python3.0导入模块查找顺序：
内存中已经加载的模块->内置模块->sys.path路径（导模块的环境变量）中包含的模块。
防止标准库模块被覆盖。

python3.0中包的导入默认是绝对的，相对导入只在包内导入使用；

'''
'''
最顶级包pack_test是写给别人用的，然后在pack_test包内部也会有彼此之间互相导入的需求，
这时候就有绝对导入和相对导入两种方式：
绝对导入：以pack_test作为起始,绝对导入的格式为 import A.B 或 from A import B;
相对导入：相对导入格式为 from .A import B 或 from .X import Y，.代表当前模块，..代表上层模块;
          相对导入可以避免硬编码带来的包维护问题，例如我们改了某一层包的名称，那么其它模块对于
          其子包的所有绝对导入就不能用了，但是采用相对导入语句的模块，就会避免这个问题。

《《《《注意：存在相对导入语句的模块，是不能直接运行的！！！！！》》》》
这是因为：一个模块直接运行，Python 认为这个模块就是顶层模块，不存在层次结构，所以找不到
其它的相对路径。
'''

from ..conf.settings import test_settings
def rl_import():
    test_settings()            #采用相对导入，不能直接运行
    print("相对导入结束!")
#测试结果：注意一定要在于 pack_test 同级的文件中测试