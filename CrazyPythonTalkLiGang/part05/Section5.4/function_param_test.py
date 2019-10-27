def map(data,fn):
    result = []
    for e in data:
        result.append(fn(e))
    return result
def square(n):
    return n*n
def cube(n):
    return n*n*n
def factorial(n):
    result = 1
    for index in range(2,n+1):
        result *= index
    return result
data = [3,4,9,5,8]
print("原数据：",data)
print("计算数组元素的平方")
print(map(data,square))
print(map(data,cube))
print(map(data,factorial))
print(type(map))