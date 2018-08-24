# Author:Jay
name = "my \tname is {name} and i am {year} old"
print(name.capitalize())#首字母大写
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ay"))
print(name.expandtabs(tabsize=30))#tab打印转换格式
print(name.find("name"))
print(name[name.find("name"):])
print(name.format(name='jay',year=23))
print(name.format_map({'name':'jay','year':14}))
print('ab123'.isalnum())#阿拉伯字母和字符
print('ab123'.isalpha())#纯英文字符
print('1A'.isdigit())#整数
print('1A'.isidentifier())#合法变量名
print('myNAme'.isupper())#大写
print(','.join(['1','2','3']))#生成字符串
print(name.ljust(50,'*'))#左对齐补充*
print('jay\n'.strip())#去掉两头空格和回车,左lstrip,右rstrip
p = str.maketrans("abcdefjy",'12345678')#编码对应规则（随机密码）
print("jay".translate(p))
print("jay".replace('j','J',1))
print('jayyang deng'.rfind('g'))
print("jang yang deng".split())
print("Jangyang Deng".swapcase())#大小写取反
print("jayyang deng".zfill(50))