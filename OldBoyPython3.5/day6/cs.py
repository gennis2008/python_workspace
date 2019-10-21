'''
# 方法一：
# role 1
name = 'Alex'
role = 'terrorist'
weapon = 'AK47'
life_value = 100
money = 10000

# role 2
name = 'cammile'
role = 'police'
weapon = 'B22'
life_value = 100
money = 10000

# role 3
name = 'jack'
role = 'terrorist'
life_value = 'c33'
money = 10000

# role 4
name = 'eric'
role = 'police'
weapon = 'B51'
life_value = 100
money = 10000

方法二：使用字典

roles = {
    1:{'name':'alex',
       'role':'terrorist',
       'life_value':100,
       'money':10000,
    },
    2:{'name':'cammile',
       'role':'police',
       'life_value':100,
       'money':10000,
    },
    3:{'name':'jack',
       'role':'terrorist',
       'life_value':100,
       'money':10000,
    },
    4:{'name':'eric',
       'role':'police',
       'life_value':100,
       'money':10000,
    },
}
'''


# 方法三：使用oop
class Role(object):
    def __init__(self,name,weapon,role,life_value,money):
        self.name = name
        self.weapon = weapon
        self.role = role
        self.life_value = life_value
        self.money = money
    def shot(self):
        print("shooting......")

    def got_shot(self):
        print("ah....,i got shot...")

    def buy_gun(self,gun_name):
        print("just though %s " % gun_name)

r1 = Role("alex","ak47","police",100,10000)
r2 = Role("jack","B51","terrosist",100,10000)
r1.shot()
r2.got_shot()



