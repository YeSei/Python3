# Author:Jay
import copy
#names = "zhangyang guyun xiangpeng xuliangchen"
#names = ["zhangyang","guyun","xiangpeng",["alex","jack"],"xuliangchen"]
#print(names)
# print(names[0])
# print(names[1:3])#切片
# print(names[-2:])#切片
# print(names[:3])#切片
# names.append("leihaidong")
# names.insert(1,"chenronghua")
#不能批量插入
# print(names)
# names[2]="xiedi"#替换
# print(names)
#names.remove("chenronghua")
#del names[1]
#names.pop(1)
# print(names)
#
# print(names.count("chenronghua"))
# names.reverse()
# print(names)
# names.sort()
# print(names)

# names2 = [1,2,3,4]
# names.extend(names2)
# print(names)

# names.clear()
# print(names)

#浅复制：只复制顶层
names = ["zhangyang","guyun","xiangpeng",["alex","jack"],"xuliangchen"]
names2 = names.copy()
print(names)
print(names2)
names[2] = "向鹏"
names[3][0] = "Alex"
print(names)
print(names2)

#深复制
names = ["zhangyang","guyun","xiangpeng",["alex","jack"],"xuliangchen"]
names2 = copy.deepcopy(names)
print(names)
print(names2)
names[2] = "向鹏"
names[3][0] = "Alex"
print(names)
print(names2)