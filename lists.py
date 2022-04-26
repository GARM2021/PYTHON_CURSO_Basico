from ast import Index
from operator import truediv


colors = ['red', 'green', 'blue', 'brown']
numbers_list = list((1, 2, 3, 4)) #!convierte una tupla en lista 

r = list(range(1, 10))

print(r)

#print (dir(colors))

#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 
#'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(colors[2])
print(colors[-2])

print('green' in colors)

print(colors)
colors[1] = 'yellow'
print(colors)

colors.append('violet')
colors.extend(['brown', 'purpule'])
print(colors)

colors.insert(1, 'black')
print(colors)

colors.insert(len(colors), 'magenta')
print(colors)

colors.remove('magenta')

colors.pop() #! cuando no lleva valor remueve el ultimo elemento

print(colors)

#colors.clear()
colors.sort()

print(colors)

colors.sort(reverse=True)

print(colors)

print(colors.index('brown'))

print(colors.count('brown'))

print(colors)




