def get_math_func(type):
    result = 1
    if type =="square":
        return lambda n:n*n
    elif type =="cube":
        return lambda n:n*n*n
    else:
        return lambda n: (1+n)*n/2
math_func = get_math_func("cube")
print(math_func(5))
math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("other")
print(math_func(5))
