# Author:Jay
import shelve
import datetime

d = shelve.open("shelve1")
'''
#shelve模块存储
info = {'age':23,"job":'it'}

name = ['jay','cool','nb']
d['name'] = name
d['info'] = info
d['date'] = datetime.datetime.now()
d.close()
'''
print(d.get("name"))
print(d.get('info'))
print(d.get('date'))