# Author:Jay
import shutil

# f1 = open("本节笔记",encoding="utf-8")
# f2 = open("笔记2",'w',encoding="utf-8")
# shutil.copyfileobj(f1,f2)
#等效如下：
shutil.copyfile('本节笔记','笔记3')

shutil.make_archive("shutil_archive_test","zip","D:\s14\day5-atm") #压缩软件