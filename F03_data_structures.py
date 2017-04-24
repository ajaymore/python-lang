__author__ = 'Mystique'

# Queue
from collections import deque

queue = deque(['Eric', 'john', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
queue.popleft()
print(queue)

# List Comprehensions
squares = list(map(lambda x: x ** 2, range(10)))
squares1 = [x ** 2 for x in range(10)]
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares)
print(squares1)
print(pairs)
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
result = [x * 2 for x in vec]
# filter the list to exclude negative numbers
result = [x for x in vec if x >= 0]
# apply a function to all the elements
result = [abs(x) for x in vec]
# call a method on each element
fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
result = [weapon.strip() for weapon in fresh_fruit]
# create a list of 2-tuples like (number, square)
result = [(x, x ** 2) for x in range(6)]
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for elem in vec for num in elem]
# complex nested
from math import pi

result = [str(round(pi, i)) for i in range(1, 6)]
print(result)
# 3*4 matrix
result = [[row * 4 + num for num in range(4)] for row in range(4)]
print(result)
print(list(zip(*result)))

# del keyword
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]
del a

# tuples
t = 12345, 54321, 'hello!'
print(t[0])
u = t, (1, 2, 3)  # nesting
print(u)
empty = ()  # empty tuple
singleton = 'one',


# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('apple' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
# dictionary constructor
dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dictionary = dict(sape=4139, guido=4127, jack=4098)
print(dictionary)

# Looping techniques

# dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# loop two or more sequences at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))