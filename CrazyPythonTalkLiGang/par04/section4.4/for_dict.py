my_dict = {'语文':89,'数学':92,'英语':80}
for key,value in my_dict.items():
    print('key:',key)
    print('value:',value)
print('------------------')
for key in my_dict.keys():
    print('key:',key)
    print('value',my_dict[key])
print("---------------------------")
for value in my_dict.values():
    print('value:',value)