# Author:Jay
import getpass
_username = "asd"
_password = "123"
username = input("username:")
password = input("password:")
if _username == username and _password == password:
    print("welcome user {username} login...".format(username=username))
else:
    print("invalid username or password!")