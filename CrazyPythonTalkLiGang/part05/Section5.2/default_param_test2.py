def printTriangle(char,height = 5):
    for i in range(1,height +1):
        for j in range(height-i):
            print(' ',end = '')
        for j in range(2 * i -1):
            print(char,end = '')
        print()
printTriangle('@',6)
printTriangle('#',height=7)
printTriangle(char='*')