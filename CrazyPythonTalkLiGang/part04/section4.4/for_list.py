
src_list = [12,45,3.4,13,'a',4,56,'crazyit',109.5]
my_sum = 0
my_count = 0

for ele in src_list:
    if isinstance(ele,int) or isinstance(ele,float):
        print(ele)
        my_sum += ele
        my_count += 1
print("总和：",my_sum)
print("平均数：",my_sum/my_count)