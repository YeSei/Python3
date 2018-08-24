# Author:Jay
import time
user,passswd = 'jay','123'
def auth(auth_type):
    print("auth type",auth_type)
    def outer_wrapper(func):
        print("outwrapper:",func)
        def wrapper(*args,**kargs):
            username = input("username:").strip()
            password = input("password:").strip()

            if user == username and passswd == password:
                print("\033[32;1muser has passed authentication\033[0m")
                res = func(*args,**kargs)
                print("-------value-------")
                return res
            else:
                exit("\033[32;1minvalid username or password\033[0m")
        return wrapper
    return outer_wrapper


def index():
    print("welcome to index page")

@auth(auth_type = 'local') #传递系数给装饰器，需要三层装饰器接受，第二层接受函数func信息
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type = 'ladp')
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()