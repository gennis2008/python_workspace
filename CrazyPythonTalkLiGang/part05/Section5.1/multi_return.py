def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):
            count += 1
            sum += e

    return sum,sum/count
my_list = [20,15,2.8,'a',35,5.9,-1.8]
tp = sum_and_avg(my_list)
print(tp)

s,avg = sum_and_avg(my_list)
print(s)
print(avg )