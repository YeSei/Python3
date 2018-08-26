# Jay
import re
r = re.match("^deng.*", "dengyangjie")
print(r.group())

r2 = re.match(".*eng.*", "dengyangjie")
print(r2.group())

r3 = re.search("da?", "dengyangjie")
print(r3)

r4 = re.findall("gj?", "dengyangjie")
print(r4)

r5 = re.search("(deng){2}", "dengyangjie dengdeng11")  # 分组匹配
print(r5)

r6 = re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)", "abcd123daf@34").groupdict()  # 分组匹配算法用处，使用?P< >语法赋值字典
print(r6)
print(r6['id'])

r7 = re.split("[0-9]","asdad2er5fgdfg")  # 分割匹配字符串
print(r7)

r8 = re.sub("[0-9]+","|","ascas132fgf4ghrt56",count=2)  # 匹配替换字符，次数默认全替换。
print(r8)
