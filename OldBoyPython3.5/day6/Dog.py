__author__ = 'gavin li'

class Dog:
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("%s:wang,wang,wang!" % self.name)

d1 = Dog("陈荣华")
d2 = Dog("")
d3 = Dog()
d4 = Dog()

d1.bulk("陈荣华")
d2.bulk("陈三炮")
d3.bulk("陈五炮")
d4.bulk("陈老炮")

