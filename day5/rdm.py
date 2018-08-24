# Author:Jay
import random
print(random.random())
print(random.uniform(1,2))#限制随机浮点数范围
print(random.randint(1,3))#随机1到3之间整数，包含3
print(random.randrange(0,100,2))#随机1到2之间偶数，不包含100

#随机验证码
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)