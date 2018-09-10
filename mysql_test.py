# Jay

import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='dyj2468..', db='cos')

cursor = conn.cursor()

#cursor.execute("create table employee (id int auto_increment primary key,name varchar(20) not null , phonenumber varchar(20) not null)")


#
# cursor.execute("update employee set phonenumber=18905601109 where name='tt'")
# cursor.execute("select * from employee")
# print(cursor.fetchall())
#
# cursor.execute("delete from employee where id=26")
# cursor.execute("select * from employee")
# print(cursor.fetchall())

cursor.execute("update employee set name = 'd3' where id = 25")
cursor.execute("select * from employee")
print(cursor.fetchall())
#
# cursor.execute("delete from employee where id = 1")
# cursor.execute("select * from employee")
# print(cursor.fetchall())
# cursor.execute("update employee set name = 'ddd' where id = 1")
# cursor.execute("select * from employee")
# print(cursor.fetchall())




conn.commit()

cursor.close()

conn.close()