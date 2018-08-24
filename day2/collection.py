# Author:Jay
list_1 = [1,3,5,6,8,9]
list_1 = set(list_1)
list_2 = set([2,3,4,5,6,7,8,9])
list_3 = set([1,3,7])
list_4 = set([5,6,8])
print(list_1,list_2)
print(list_1.intersection(list_2))#交集
print(list_1 & list_2)
print(list_1.union(list_2))#并集
print(list_1 | list_2)
print(list_1.difference(list_2))#差集 in list1 but not in list2
print(list_1 - list_2)
print(list_1.issubset(list_2))#判断是否子集
print(list_1.issuperset(list_2))#是否父集
print(list_1.symmetric_difference(list_2))#对称差集（去掉都有的，留下独一的）
print(list_1 ^ list_2)

print(list_3.isdisjoint(list_4))#交集测试

list_1.add("x")
list_1.update('a','s','d')
print(list_1)

print(list_1.pop())
list_1.discard('k')#删除指定值，没有也不报错
print(list_1)

#print(list_1,type(list_1))