# _*_coding:utf-8 _*_
__author__ = 'Jay'

mod = __import__("lm.aa")
print(mod)  # 这里mod是导入的lm模块，而不是aa模块。

print(mod.aa.c)  # 必须使用基于第一个模块lm来使用属性运算符.进行访问。



# 官方建议方式：
import importlib
lib = importlib.import_module('lm.aa')  # 注意！！这里lib直接是要导入的模块！
print(lib)
print(lib.c)