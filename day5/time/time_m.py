import time
import datetime
x = time.localtime()
print(time.strftime("%y-%m-%d %h:%M:%S",x))

y= datetime.datetime.now()
print(y)
print(y+datetime.timedelta(3)) #三天后时间
