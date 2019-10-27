
def pow(base,exponent):
    result  = 1
    for i in range(1,exponent+1):
        result *= base
    return result
my_fun = pow
print(my_fun(3,4))

def area(width,height):
    return width*height
my_fun = area
print(my_fun(3,4))
