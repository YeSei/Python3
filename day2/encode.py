# Author:Jay
#python3所有字符编码默认unicode格式!!!!!!
import sys
print(sys.getdefaultencoding())       #encode（）参数空时默认utf-8格式
s = "你好"
s_gbk = s.encode("gbk")              #unicode转成gbk格式
print(s_gbk)                          #gbk包括格式
print(s.encode())                     #utf-8

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")#gbk转成utf8跟上部比较
print(gbk_to_utf8)

'''附：右下角显示本文件编码格式，
若使用gbk,则python3不能识别，需要在文件头以#-*-coding:gbk-*-格式声明告诉python本文件的编码
'''