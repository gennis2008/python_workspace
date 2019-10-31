vals = 10,20,30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1,10,2))
a,b,c,d,e = a_tuple
print(a,b,c,d,e)
a_list = ['fkit','crazyit']
a_str,b_str = a_list
print(a_str,b_str)


first,second,*rest = range(10)
print(first)
print(second)
print(rest)

*begin,last = range(10)
print(begin)
print(last)
first,*middle,last = range(10)
print(first)
print(middle)
print(last)