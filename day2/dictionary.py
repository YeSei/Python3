# Author:Jay
info = {
    'stu1101':"tenglan wu",
    'stu1102':"longze luola",
    'stu1103':"xiaoze maliya",
}
# print(info)
# print(info.get("stu1105"))
# print("stu1103"in info)
# print(info["stu1101"])
# info["stu1101"] = "武藤兰"
# info["stu1104"] = "cangjingkong"
# del info["syu1101"]#删除一个
# info.pop("stu1101")
# print(info)

b = {
    'stu1101':'jay',
    1:2,
    2:3,
}
info.update(b)#更新合并列表
print(info)

print(info.items())

c = dict.fromkeys([6,7,8],"initial")
print(c)
d = dict.fromkeys([6,7,8],[1,{"name":"jay"},444])
print(d)
d[7][1]["name"] = "jack"#可变参数的后遗症
print(d)

for i in info:#迭代器
    print(i,info[i])

for k,v in info.items():#创建更多对象，占有更多内存
    print(k,v)