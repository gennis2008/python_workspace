def test(a,*books):
    print(books)
    for b in books:
        print(b)
    print(a)

test(5,"疯狂ios讲义","疯狂Android讲义")
