name = 'Charlie'
def test():
    print(globals()['name'])
    name = '孙悟空'

test()
print(name)