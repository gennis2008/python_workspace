def my_max(x,y):
    z = x if x>y else y
    return z
def say_hi(name):
    print("正在执行say_hi()函数====")
    return name + ",你好！"
def my_max_change(x,y):
    return x if x > y else y

a = 6
b = 9
result = my_max(a,b)
result1 = my_max_change(a,b)
print("result:",result)
print("result_change",result1)
print(say_hi('fkit'))