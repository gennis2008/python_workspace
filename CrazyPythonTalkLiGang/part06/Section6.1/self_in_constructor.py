class InConstructor:
    def __init__(self):
        #在构造方法中定义一个foo变量（局部变量）
        foo = 0
        #使用self方法代表该构造方法正在初始化的对象
        #下面的代码将会把该构造方法正在初始化的对角foo变量设置为6
        self.foo = 6
print(InConstructor().foo)