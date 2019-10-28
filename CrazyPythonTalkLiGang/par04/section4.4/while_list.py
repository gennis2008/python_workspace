src_list = [12,45,34,13,100,23,56,74,109]
a_list = []
b_list = []
c_list = []
while len(src_list) >0:
    ele = src_list.pop()
    if ele %3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3：",a_list)
print("整除3余1",b_list)
print("整除3余2",c_list)