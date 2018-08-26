__author__ = "Jay"

import configparser

conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.defaults())
print(conf['bitbucket.org']['user'])
#print(conf.sections())
sec = conf.remove_section('bitbucket.org')  #删除某属性
conf.write(open('example.ini', "w"))