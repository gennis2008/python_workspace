
order_endings = ('str','nd','rd')\
    + ('th',)*17 + ('st','nd','rd')\
    +('th',)*7 + ('st',)
print(order_endings)

day = input("输入日期：(1-31):")
day_int = int(day)
print(day+order_endings[day_int-1])