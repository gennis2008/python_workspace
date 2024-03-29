def get_math_func(type):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    def factorial(n):
        result = 1
        for index in range(2,n+1):
            result *= index
        return result
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial
math_func = get_math_func("cube")
print(math_func(5))

math_func = get_math_func("square")
print(math_func(5))

math_func = get_math_func("other")
print(math_func(5))