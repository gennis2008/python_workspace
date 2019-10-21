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
    def piao(self):
        print("%s piao....." % self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleep.....")

m1 = People("gavin",40)
m1.eat()
m1.sleep()
m1.talk()

m2 = Man("elaine",38)
m2.sleep()
m2.eat()