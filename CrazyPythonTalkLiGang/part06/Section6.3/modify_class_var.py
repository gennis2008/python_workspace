class Inventory:
    item = 'mouse'
    quantity = 2000
    def change(self,item,quantity):
        self.item = item
        self.quantity = quantity

iv = Inventory()
iv.change('display',500)
print(iv.item)
print(iv.quantity)

print(Inventory.item)
print(Inventory.quantity)

iv.item = '实例变量item'
iv.quantity = '实例变量quantity'

print(Inventory.item)
print(Inventory.quantity)