# Author:Jay
#while循环使用
# age_of_oldboy = 56
# cout = 3
# while cout:
#     guess_age = int(input("guess age:"))
#     if guess_age == age_of_oldboy:
#         print("yes,you get it!")
#         break
#     elif guess_age>age_of_oldboy:
#         print("think smaller...")
#     else:
#         print("think bigger")
#     cout -=1
#     if cout == 0:
#         countine_confirm = input("do you want to continue??")
#         if countine_confirm != 'n':
#             cout = 3
# else:
#     print("you have try so many times")


#for循环使用
# for i in range(3):
#     guess_age = int(input("guess age:"))
#     if guess_age == age_of_oldboy:
#         print("yes,you get it!")
#         break
#     elif guess_age>age_of_oldboy:
#         print("think smaller...")
#     else:
#         print("think bigger")
# else:
#     print("you have try so many times")

#continue使用
# for i in range(0,10):
#     if i < 5:
#         print("loop",i)
#     else:
#         continue
#     print("hehe...")

for i in range(10):
    print('----------------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break