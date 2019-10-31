a_list = [3,4,-2,-30,14,9.3,3.4]
a_list.sort()
print(a_list)
b_list = ['python','swift','ruby','go','kotline','erlang']
b_list.sort()
print(b_list)

b_list.sort(key=len)
print(b_list)
b_list.sort(key=len,reverse=True)
print(b_list)