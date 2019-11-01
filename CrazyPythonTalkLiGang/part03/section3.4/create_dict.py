scores = {"语文":89,'数学':92,'英语':93}
print(scores)
empty_dict = {}
print(empty_dict)
dict2 = {(20,30):'good',30:'bad'}
print(dict2)

vegetables = [('celery',1.58),('brocoli',1.29),('lettuce',2.19)]
dict3 = dict(vegetables)
print(dict3)

cars = [['bmw',8.5],['bens',8.3],['audi',7.9]]
dict4 = dict(cars)
print(dict4)
dict5 =dict()
print(dict5)

print('*********************')
dict6 = dict(spinach = 1.39,cabbage = 2.59)
print(dict6)

print(scores['语文'])
scores['数学'] = 93
scores[92] = 5.7
print(scores)

del scores[92]
print(scores)

cars