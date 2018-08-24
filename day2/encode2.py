# Author:Jay
#-*-coding:gbk-*-
'''注意区分文件编码，和python3默认字符编码，python3中字符串永远为unicode编码。
文件编码格式可以更改，并在头部声明'''
import sys
print(sys.getdefaultencoding())       #encode（）参数空时默认utf-8格式
s = "你好"
print(s)
'''附：右下角显示本文件编码格式，
若使用gbk,则python3不能识别，需要在文件头以#-*-coding:gbk-*-格式声明告诉python本文件的编码
'''