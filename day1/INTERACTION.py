# Author:Jay
#username = input("username:")
#print(username)
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")
info2 = '''
------info of {_name}-------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}'''.format(_name = name,_age = age, _job = job,_salary = salary)
print(info2)