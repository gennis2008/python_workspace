def swap(dw):
    dw['a'],dw['b'] = dw['b'],dw['a']
    print("在swap()函数里,a元素的值是:",dw['a'],"; b元素的值是",dw['b'])
    dw = None

dw = {'a':6,'b':9}
swap(dw)
print("交换结束后，a元素的值是:",dw['a'],"; b元素的值是：",dw['b'])

