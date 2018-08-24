# Author:Jay
#三级菜单
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"],
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"advent","飞信"}
        },
    },
    '山东':{},
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    }
}
exir_flag = True
while exir_flag:
    for i in data:#显示一级选项
        print(i)
    choice = input("选择一级菜单,按q/b退出》:")
    if choice in data:
        while exir_flag:
            for i2 in data[choice]:#显示二级选项
                print("\t",i2)
            choice2 = input("选择二级菜单,按q退出，按b返回》：")
            if choice2 in data[choice]:
                while exir_flag:
                    for i3 in data[choice][choice2]:#显示三级菜单
                        print("\t\t",i3)
                    choice3 = input("选择三级菜单,按q退出，按b返回》：")
                    if choice3 in data[choice][choice2]:
                        while exir_flag:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t\t",i4)
                            choice4 = input("最后一层，按q退出，按b返回》：")
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exir_flag = False
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exir_flag = False
            if choice2 == "b":
                break
            elif choice2 == "q":
                exir_flag = False
    if choice == "b":
        break
    elif choice == "q":
        exir_flag = False