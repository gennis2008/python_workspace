def my_max(x,y):
    '''
    获取两个数值之间较大数的函数
    my_myx(x,y)
        返回x,y两个参数之间较大的那个数
    :param x: 
    :param y: 
    :return: 
    '''
    #定议一个变量z,该变量等于x,y中较大的值
    z = x if x > y else y
    # 返回变量z的值
    return z
help(my_max)
#print(my_max.__doc__)
