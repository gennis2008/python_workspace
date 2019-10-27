
def test():
    age = 20
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age']
    locals()['age'] = 12
    print('xxx',age)
    globals()['x'] = 19
test()
print('********')
x = 5
y = 20
print(globals())
print(locals())
print(x)
print(globals()['x'])

globals()['x'] = 39
print(x)

locals()['x'] = 99
print(x)
