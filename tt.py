
import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='dyj2468..', db='cos')

cursor = conn.cursor()

cursor.execute("insert into employee(name,phonenumber) values ('tt','189 you guess 1109')")
cursor.execute("select * from employee")
print(cursor.fetchall())

cursor.execute("insert into employee(name,phonenumber)values('ll','123456789')")
cursor.execute("select * from employee")
print(cursor.fetchall())


cursor.execute("delete from employee where name='tt'")
cursor.execute("select * from employee")
print(cursor.fetchall())

cursor.execute("update employee set phonenumber='23456789' where name='ll'")
cursor.execute("select * from employee")
print(cursor.fetchall()
)

# effect1 = cursor.execute("select * from employee")
# print(effect1)a
# print(cursor.fetchone())
#
#
# print(cursor.fetchall())

# cursor.execute("update employee set phonenumber=18905601109 where name='tt'")
# cursor.execute("select * from employee")
# print(cursor.fetchall())
#
# cursor.execute("delete from employee")
# cursor.execute("select * from employee")
# print(cursor.fetchall())

# cursor.execute("update employee set name = 'd3' where id = 1")
# cursor.execute("select * from employee")
# print(cursor.fetchall())
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