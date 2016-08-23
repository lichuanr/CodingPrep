

#1.1 The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
#Add an item to the end of the list; equivalent to a[len(a):] = [x].

list.extend(L)
#Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

list.insert(i, x)
#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
#Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.index(x)
#Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x)
#Return the number of times x appears in the list.

list.sort(cmp=None, key=None, reverse=False)
#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
#Reverse the elements of the list, in place.

#Examples
>>> a = [66.25, 333, 333, 1, 1234.5]
>>> print a.count(333), a.count(66.25), a.count('x')
2 1 0
>>> a.insert(2, -1)
>>> a.append(333)
>>> a
[66.25, 333, -1, 333, 1, 1234.5, 333]
>>> a.index(333)
1
>>> a.remove(333)
>>> a
[66.25, -1, 333, 1, 1234.5, 333]
>>> a.reverse()
>>> a
[333, 1234.5, 1, 333, -1, 66.25]
>>> a.sort()
>>> a
[-1, 1, 66.25, 333, 333, 1234.5]
>>> a.pop()
1234.5
>>> a
[-1, 1, 66.25, 333, 333]




#1.2 Functional Programming Tools 
#There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce().

#filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. 
# If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list. 
# For example, to compute a sequence of numbers divisible by 3 or 5:

#Examples
>>> def f(x): return x % 3 == 0 or x % 5 == 0
...
>>> filter(f, range(2, 25))
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

#map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values. 
#For example, to compute some cubes:

#Examples
>>> def cube(x): return x*x*x
...
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#Examples
>>> seq = range(8)
>>> def add(x, y): return x+y
...
>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]



#reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. 
#DDesc Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.

#For example, to compute the sum of the numbers 1 through 10:

>>>
>>> def add(x,y): return x+y
...
>>> reduce(add, range(1, 11))
55


#1.3 list comprehension

#Examples
squares = [x**2 for x in range(10)]
# equivalent to 
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
#equivalent to funtional programming 
squares = map(lambda x: x**2, range(10))
#Result:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#Examples
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# equivalent to
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


#Examples
# 1.3 Nested list comprehension
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
# equivalent to 
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# equivalent to 
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# equivalent to 
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# equivalent to 
>>> zip(*matrix)
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
#Explaination:
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True


#1.4 The del statement
#There is a way to remove an item from a list given its index instead of its value: the del statement. 

#Examples
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]


#1.5 tuples 
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])


#1.6 
#A set is an unordered collection with no duplicate elements
# Basic operations:
# len(s)
# x in s
# x not in s
# isdisjoint(other)
# issubset(other)
# set <= other
# set < other
# issuperset(other)
# set >= other
# set > other
# union(other, ...)
# set | other | ...
# intersection(other, ...)
# set & other & ...
# difference(other, ...)
# set - other - ...
# symmetric_difference(other)
# set ^ other
# copy()
#     Return a new set with a shallow copy of s.

#Examples
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> fruit = set(basket)               # create a set without duplicates
>>> fruit
set(['orange', 'pear', 'apple', 'banana'])
>>> 'orange' in fruit                 # fast membership testing
True
>>> 'crabgrass' in fruit
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])



#1.7 looping technique

#Example:
#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print i, v
...
0 tic
1 tac
2 toe

#Example:
#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
>>> for i in reversed(xrange(1,10,2)):
...     print i
...
9
7
5
3
1

equivalent to:  for i in range(len(lst)-1,-1,-1):


#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print f
...
apple
banana
orange
pear


#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.
>>>
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():
...     print k, v
...
gallahad the pure
robin the brave
It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]