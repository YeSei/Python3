# Jay


class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s : wang wang wang!! " % self.name)


d1 = Dog("w1")
d2 = Dog("w2")
d3 = Dog("w3")
d4 = Dog("w4")

d1.bulk()
d2.bulk()
d3.bulk()
d4.bulk()
