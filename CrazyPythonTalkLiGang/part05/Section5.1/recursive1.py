def fn(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    else:
        return fn(n+2) - 2*fn(n+1)

print("fn(10)的值是：",fn(1))