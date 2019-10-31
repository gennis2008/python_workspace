def girth(width,height):
    print("width:",width)
    print("height",height)
    return 2 * (width+height)

print(girth(3.5,4.8))
print(girth(width=3.5,height=4.8))
print(girth(height=4.8,width=3.5))
print(girth(3.5,height=4.8))

# 报错，默认参数需排在前面
# print(girth(width=3.5,4.8))
