class Bird:
    @classmethod
    def fly(cls):
        print("类方法fly",cls)
    @staticmethod
    def info(p):
        print("静态方法info",p)
Bird().fly()
Bird().info("crazyit")

b = Bird()
b.fly()
b.info("fkit")