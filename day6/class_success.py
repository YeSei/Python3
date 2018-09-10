# Jay

# class People: 经典类
class People(object):  # 新式类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


class Relation(object):
    # def __init__(self, n1,n2):
    #     self.cla = n1
    #     print("relationship:%s" % self.cla)

    def make_friends(self, obj): #w1
        print("%s is making friends with %s" % (self.name,obj.name))
        self.friends.append(obj)


class Man(Relation,People):

    # def __init__(self,name,age,money):
    #     #People.__init__(self,name,age)
    #     super(Man,self).__init__(name,age) #python3经典和新式类采用广度优先遍历。python2经典类按深度优先继承，新式类按广度优先。
    #     优点：1：改父类不用改子类，
    #     2：采用super方式会自动找到从左向后多继承中的第一个父类的init，若无，则向后查找，如果还想强制调用后续父类init，就要用相应父类名进行调用。
    #     注意！！只找多继承的第一个


    #     #self.money  = money
    #     #print("%s 一出生就有%s money" %(self.name,self.age))
    def __init__(self,name, age, money):
        super(Man,self).__init__(name,age)
        self.money = money

    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping ")


class Woman(People, Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)

q1 = Man("dyj",23,20)
q2 = Woman("d2",23)
q1.make_friends(q2)

# m1 = Man("NiuHanYang",22)
# w1 = Woman("ChenRonghua",26)
#
# m1.make_friends(w1)
# w1.name = "陈三炮"
# print(m1.friends[0].name)
