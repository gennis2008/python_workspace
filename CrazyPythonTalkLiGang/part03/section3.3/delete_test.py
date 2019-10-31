a_list = ['crazyit',20,-2.4,(3,4),'fkit']
del a_list[2]
print(a_list)

del a_list[1:3]
print(a_list)

b_list = list(range(1,10))
print(b_list)
del b_list[2:-2:2]
print(b_list)

del b_list[2:4]
print(b_list)

name = 'crazyit'
print(name)
del name
# print(name)

c_list = [20,'crazyit',30,-4,'crazyit',3.4]
c_list.remove(30)
print(c_list)
c_list.remove('crazyit')
print(c_list)

c_list.clear()
print(c_list)