# _*_coding:utf-8 _*_
__author__ = 'Jay'


names = [1,2]

try:
    names[3]
except IndexError as e:
    print("没有这个索引：%s" %e)
except Exception:                # 捕捉所有异常,一般用于结尾。
    pass

class jayexception(Exception):   # 自定义的异常
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    raise jayexception("jay's joke")
except jayexception as e:
    print(e)
