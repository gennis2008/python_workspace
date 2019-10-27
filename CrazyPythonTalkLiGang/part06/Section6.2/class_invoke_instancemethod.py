class User:
    def walk(self):
        print(self,"正慢慢的走")

# 通过类调用实例方法
# User.walk()
'''
python类可以调用实例方法，但使用类调用实例方法时，Python不会自动为方法的第一个参数self绑定参数值;
程序必须显式地为第一个参数self传入方法调用者。这种调用方式被称为“未绑定方法”。
'''
u = User()
u.walk()
User.walk(u)
User.walk('fkit')