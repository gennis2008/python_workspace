def test(*books,num):
    print(books)
    for b in books:
        print(b)

    print(num)

test("疯狂ios讲义","疯狂Android讲义",num = 20)
