src_list = [12,45,3.4,12,'fkit',45,3.4,'fkit',45,3.4]
sattistics = {}
for ele in src_list:
    if ele in sattistics:
        sattistics[ele] += 1
    else:
        sattistics[ele] = 1
for ele,count in sattistics.items():
    print("%s出现的次为：%d"% (ele,count))