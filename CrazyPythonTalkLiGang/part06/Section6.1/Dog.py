class Dog:
    #定义一个jump方法
    def jump(self):
        print("正在执行jump方法")
    def run(self):
        self.jump()
        print("正在执行run方法")

p = Dog()
p.run()
print("---------")
p.jump()