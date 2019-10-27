def test(name,message):
    print("用户是：" , name)
    print("欢迎消息是：",message)

my_list = ['孙悟空','欢迎来疯狂软件']
test(*my_list)
print('*****')
# ###########################
def foo(name,*nums):
    print("name参数：",name)
    print("nums参数:",nums)
my_tuple = (1,2,3)

foo('fkit',*my_tuple)
print('********')
foo(*my_tuple)
print('*******')
foo(my_tuple)
#############################

def bar(book,price,desc):
    print(book,'这本书的价格是：',price)
    print('描述信息是：',desc)

print('********')
my_dict = {'price':89,'book':'疯狂python讲义','desc':'这是一本系统全面的python学习图书'}
bar(**my_dict)
print('*******')
#如果是下面的调用形式，不采用逆向参数收集将报错
# TypeError: bar() missing 2 required positional arguments: 'price' and 'desc'
bar(my_dict)