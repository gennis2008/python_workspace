a_list = [2,4,-3.4,'crazyit',23]
a_list[2] = 'fkit'
print(a_list)
a_list[-2] = 9527
print(a_list)

b_list = list(range(1,5))
print(b_list)
b_list[1:3] = ['a','b']
print(b_list)
b_list[2:5] = []
print(b_list)
b_list[2:2] = ['x','y']
print(b_list)
b_list[1:3]='charlie'
print(b_list)

c_list = list(range(1,10))
c_list[2:9:2]=['a','b','c','d']
print(c_list)