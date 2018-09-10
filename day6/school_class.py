# Jay
class school(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staff = []

    def enroll(self, stu_obj):
        print("为%s办理注册" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣%s" % staff_obj.name)
        self.staff.append(staff_obj)


class schoolmember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = age

    def tell(self):
        pass


class teacher(schoolmember):

    def __init__(self, name, age, sex, salary, course):
        super(teacher, self).__init__(name, age, sex,)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ----info of teacher----
        name:%s
        age:%s
        sex:%s
        salary:%s
        course:%s
        ''' % (self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s teaching course:%s" % (self.name, self.course))


class student(schoolmember):

    def __init__(self, name, age, sex, stu_id, grade):
        super(student, self).__init__(name, age, sex, )
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ----info of student----
        name:%s
        age:%s
        sex:%s
        stu_id:%s
        grade:%s
        ''' % (self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tution(self,amout):
        print("%s has paid tution for %s" % (self.name, amout))


school = school("ustc","沙河")

t1 = teacher("dyj1",23,"M",3000,"python")
t2 = teacher("dyj2",23,"M",4000,"linux")

t1.tell()

s1 = student("d1",23,"W",1001,"python")
s2 = student("d2",23,"M",1002,"linux")

s2.tell()

school.hire(t1)
school.hire(t2)
school.enroll(s1)
school.enroll(s2)

'''
for stu in school.students:
    print(stu.pay_tution(2000))

for tea in school.staff:
    print(tea.teach())
这里会输出相应函数后，接着输出None，然后交替输出，
原因在于：其调用函数有输出语句且函数无返回值,即为None！
'''
for stu in school.students:
    stu.pay_tution(2000)

for tea in school.staff:
    tea.teach()

tt = []
tt.append("11")
tt.append("22")
for t in tt:
    print(t)
print(len(tt))
