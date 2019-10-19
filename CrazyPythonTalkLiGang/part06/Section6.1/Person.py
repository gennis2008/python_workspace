class Person:
    '这是学习python类定义的第一个Person类'
    # 下面定义一下类变量
    hair = 'black'
    def __init__(self,name='gavin',age=20):
        # 下面为Person对象增加两个实例变量
        self.name = name
        self.age = age
    # 下面定义一个say方法
    def say(self,content):
        print(content)

# 调用Person类的构造方法，返回一个Person对象
# 将Person对象赋值给P变量

p = Person()

# 输出P对象的名字和年龄
print(p.name,p.age)

p.name = 'gennis2008'

print(p.name)

p.say('Python语言很简单，学习很容易！')

p.skills = ['programming','swimming']
print(p.skills)

del p.name

# 先定义一下函数
def info(self):
    print("-----info-----函数",self)

# 使用info对象对p的的foo方法赋值(动态增加方法)
p.foo = info
#python不会自动将调用者绑定到第一个参数
#因此程序需要手动将调用者绑定到第一个参数
p.foo(p)

#使用lambda表达式为p对象的bar方法赋值（动态增加方法）
p.bar = lambda self:print("---lambda表达式----",self)
p.bar(p)

def intro_func(self,content):
    print ("我是一个人，信息为：%s" % content)
# 导入MethodType
from types import MethodType
#使用MethodType对intro_func进行包装，将函数的第一个参数绑定为p
p.intro = MethodType(intro_func,p)
#第一参数已绑定了，无需传入
p.intro("生活在别处")