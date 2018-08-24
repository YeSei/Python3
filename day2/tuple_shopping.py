# Author:Jay
#购物车程序
product_list = [
    ('iphone',5800),
    ('mac pro',9800),
    ('bike',800),
    ('watch',10600),
    ('coffe',31),
    ('alex python',120),
]
shopping_list = []
salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("选择要买什么,输入q退出》》")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:#买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    #着色格式：\033[41;1m这里填入着色内容\033[0m
                    print("ADD %s into shopping cart,your current balance is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线啊\033[0m" % salary)
            else:
                print("product code [%s] is not exist!"%user_choice)
        elif user_choice == 'q':
            print("--------shopping list--------")
            for p in shopping_list:
                print(p)
            print("your current balance:",salary)
        else:
            print("invalid option")
else:
    print("input salary is wrong!")