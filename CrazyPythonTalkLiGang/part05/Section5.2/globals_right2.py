name = 'Charlie'
def test():
    global name
    print(name)
    name = "孙悟空"

test()
print(name)