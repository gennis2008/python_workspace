
def foo():
    name = 'Charlie'
    def bar():
        nonlocal name
        print(name)
        name = '孙悟空'
    bar()

foo()