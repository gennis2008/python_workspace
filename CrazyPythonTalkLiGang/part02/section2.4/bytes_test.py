b1 = bytes()
b2 = b''
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
b4 = bytes('我爱python编程',encoding='utf-8')
print(b4)
b5 ='学习python很有趣'.encode('utf-8')
print(b5)

st = b5.decode('utf-8')
print(st)

ss = 'Hello\nCharlie\nGood\nMorning'
print(ss)

ss2 = '商品名\t\t单价\t\t数量\t\t总价'
ss3 = '疯狂Java讲义\t108\t\t2\t\t216'
print(ss2)
print(ss3)

price = 108
print("the book's price is %s" % price)

num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)
print("num is: %6f" % num)
print('*******************')
print("num is: %06i" % num)
print("num is: %+6i" % num)
print("num is: %-6i" % num)

my_value = 3.001415926535
print("my value is:%8.3f" % my_value)
print("my value is:%+08.3f" % my_value)
print("my value is:%08.3f" % my_value)
print("my value is:%.3f" % my_value)
print("my value is:%10.2f" % my_value)
print("my value is:%8.3f" % my_value)

