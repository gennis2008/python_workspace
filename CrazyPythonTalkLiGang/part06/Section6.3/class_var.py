class Address:
    detail = '广州'
    post_code = '510660'
    def info(self):
        #print(detail) 报错
        print(Address.detail)
        print(Address.post_code)
        print("对象",self.detail)
        print('对象',self.post_code)
print(Address.detail)
addr = Address()
addr.info()

Address.detail = '佛山'
Address.post_code = '460110'
addr.info()

addr.detail = '中山'
addr.post_code = '518003'
addr.info()