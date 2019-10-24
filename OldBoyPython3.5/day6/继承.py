class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s eat....." % self.name)
    def sleep(self):
        print("%s sleep ...." % self.name)

    def talk(self):
        print("%s talk ....." % self.name)

class Man(People):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.money = money
        print("出生就有钱")
    def piao(self):
        print("%s piao....." % self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleep.....")

class Woman(People):
    def get_birth(self):
        print("%s borth a baby" % self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is makeing friends with %s" %(self.name,obj.name))
        self.

m1 = People("gavin",40)
m1.eat()
m1.sleep()
m1.talk()

m2 = Man("elaine",38,10)
m2.sleep()
m2.eat()

w1 = Woman("chenxx",30)
w1.get_birth()