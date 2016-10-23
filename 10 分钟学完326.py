"""
#lecture 1
print 'he' * 3
import math
print type(math)
#<type 'module'> 
print math
#<module 'math' (built-in)> 
def print_lyrics():
    pass

print print_lyrics
#<function print_lyrics at 0x7f457ad5d398> 
print type(print_lyrics)
#<type 'function'> 

#lecture 2
#recursion example
def count_down(n):
    if n <= 0:
        print "stop"
    else:
        print n,
        count_down(n-1)
        
count_down(9)


def factorial(n):
    if not isinstance(n, int):
        return None
    elif n <= 0:
        return 1
    else:
        return n*factorial(n-1)
print factorial(4)

#string slicing
str1 = "chuanrui"
#end point exclusive
print str1[0], str1[:1], str1[1:], str1[:]

#string subset
if "a" in "abc":
    print True
    
#is identity testing, == is equality testing
str1, str2 = 'hello', 'he'+'llo'
print str1 == str2
print str1 is str2

a = 'pub'
b = ''.join(['p', 'u', 'b'])
print a is b


#lecture3
print [1, 2, 3] + [4, 5, 6]
print [1, 2, 3] * 3

#[1, 2, 3] -> [5, 6]
lst = [1, 2, 3, 4]
lst[0:3] = [5, 6]
print lst



#lecture4
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n in [0, 1]:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result
    
print fibonacci(4)


#immutable data structure
#int, tuple, string

qnot, rem = divmod(7, 3)
print qnot, rem


#lecture5
l1 = [1, 2, 3, 4, 5]
l2 = [i*2 for i in l1]
print l2

l2 = [x*x for x in range(10)]
print l2

l2 = [x for x in l1 if x % 2 == 0]
print l2

def p(x):
    if x > 2:
        return x

l2 = [x for x in l1 if p(x)]
print l2


l3, l4 = [1, 2, 3], [4, 5, 6]
l2 = [(x, y) for x in l4 for y in l3]
print l2
#[(4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (6, 3)] 


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [i[2] for i in m1]
#[3, 6, 9] 

#quick sort 
def qsort(s):
    if len(s) == 1 or len(s) == 0: 
        return s
    pivot = s[0]
    return qsort([l for l in s if l < pivot]) + [l for l in s if l == pivot] + qsort([l for l in s if l > pivot])

print qsort([2, 4, 9, 1, 3, 0])



#lecture6
#n-rank == n-dimension
rank2 = [[1, 2, 3], [4, 5, 6]]
rank3 = [[[1], [2]],[[1], [2]]]


import numpy as np
#5 rows, 2 column
#Super important -> arange starts from 0
a = np.arange(10).reshape(5, 2)
print a.ndim, a.shape
print a

b = np.array([(1.5, 2, 3),(4, 5, 6)])
print b

#empty == zero
print np.zeros((3, 4))
print np.empty((2, 3))

#2 list, 3 rows, 4 columns -> 3-dimension
print np.ones((2, 3, 4), dtype = 'int16')

print np.random.random((2, 3))


print np.arange(10, 30, 5)
#[10 15 20 25] -> last one is exclusive, 5 is step

print np.linspace(0, 2, 9)
#[ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ] -> 9 elements

print a.ravel()
#[0 1 2 3 4 5 6 7 8 9] 


#Lecture7
import numpy as np
a = np.arange(10).reshape(2, 5)

#resize change array A itself, does not return anything
#reshape does not change array A, return new reshaped array
c = a.resize(1, 10)
print c, a 
#None,resized A 

c = a.reshape(2, 5)
print c, a 
#reshaped array, A

print a.reshape(1, -1) 
#this is same as a.reshape(1, 10)

#broadcast
a = np.array([0, 1, 8, 27, 64, 125, 216, 343])
a[0:6:2] = 1000
print a
#[1000    1 1000   27 1000  125  216  343] 

print a[::-1], a

#ending point is always exclusive
a = np.arange(16).reshape(4, 4)
print "1:", a[1:3, :]
#[[ 4  5  6  7] [ 8  9 10 11]] 
print "2:", a[:, 1]
# [1  5  9 13] 
print "3:", a[-1]
#last row [12 13 14 15] 

#lecture 8

# Operator:
# Calculate from right to left 

# v5 -> 1, 2, 3, 4, 5 
# #starting from 1

# +/ v5 -> 15
# #sum

# +\ v5 -> 1 3 6 10 15
# #partial sum

# +/ +\ v5 -> 35

# reverse -> special symbol

# 5 & 6 -> 6 6 6 6 6

# */ 5 & 2 -> 2*2*2*2*2
# #2**5
import numpy as np
a = np.arange(5)
#[0 1 2 3 4]
print np.add.reduce(a)
#10
print np.add.accumulate(a)
#[0 1  3  6  10]

a = np.array([1]*10)
print np.add.accumulate(a)
#[1 2 3  4  5 6 7  8  9  10]

#Lecture9
import numpy as np
a, b = [1, 2, 3], [4, 5, 6]
print [i+j for i, j in zip(a, b)]

c, d = np.array([4, 5, 6]), np.arange(3)
print c - d
#[4 4 4]

print np.array([1, 2, 3])** np.array([2, 2, 2])
#[1 4 9]

e = np.arange(8) ** 2
index = np.array([1, 1, 3, 7, 5])
print e
#[ 0  1  4  9 16 25 36 49] 
print e[index]
#[ 1  1  9 49 25] 


a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
img = np.array([[1, 0, 2], [2, 2, 0]])
print a[img] #-> 3-dimension array
# [[[3 4 5] 
#   [0 1 2] 
#   [6 7 8]] 
#  [[6 7 8] 
#   [6 7 8] 
#   [0 1 2]]] 

a = np.arange(5)
a[[1, 3, 4]] = 0
print a
#[0 0 2 0 0]

a = np.arange(5)
#a[given index] = given value for these indexes
a[[0, 0, 2]] = [1, 2, 3]
print a
#[2 1 3 3 4]

#Lecture10
import numpy as np
#array of boolen as index
a = np.arange(12).reshape(3, 4)
b = a > 4
a[b] = 0
print b, a
# [[False False False False] 
#  [False  True  True  True] 
#  [ True  True  True  True]] 
# [[0 1 2 3] 
#  [4 0 0 0] 
#  [0 0 0 0]] 

re = np.linspace(-2, 1, 10)
print re

#we can think this as array of tuple and 3*2 = 6 tuples
[[(1, 1), (2, 1), (3, 1)],[(1, 2), (2, 2), (3, 2)]]

x, y = np.meshgrid([1, 2, 3], [1, 2])
print x
[[1, 2, 3], [1, 2, 3]]
print y
[[1, 1, 1], [2, 2, 2]]

#array copy
a = np.array([[1, 2],[5, 6]])
c = a.copy()
c[1,1] = 0
#only c value has been changed
print a, c

#Lecture11
import numpy as np
a = np.zeros((4, 4))
a[1, 0] = 1
a[0, 2] = 1
a[2, 2] = 1
print a
#in-degree
print np.add.reduce(a, axis = 0)
#out-degree
print np.add.reduce(a, axis = 1)

#number of edges
print np.add.reduce(np.add.reduce(a, axis = 0))


#Lecture12
#method1
def fib(n):
""" 
    # >>> fib(1)
    # 0
    # >>> fib(2)
    # 1
"""
    1
    if n == 1:
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

#method2
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
        
    def test(self):
        self.assertNotEqual(fun(2), 4)  
        
if __name__ == '__main__':
    unittest.main()


#lecture 13
#this write operation will overwrite origin content, not append
font = open('file.txt', 'w')
print font
#<open file 'file.txt', mode 'w' at 0x7f4b0c140db0> 
line = "richard"
font.write(line)
font.close()

print 'I am a %d %s'%(22223, "guy")

import os
cmd = os.getcwd()
print cmd
#print the path of the current location
#/home/coderpad 

os.path.abspath('a.txt')

#return T or F
os.path.exists('a.txt')
#True
os.path.isdir('a.txt')
#False
os.path.isfile('a.txt')
#True


#lecture 14
import redis
r_server = redis.Redis('localhost')

r_server.set("name", "value")

r_server.get("name")
#value

r_server.set("hit_counter", 1)
r_server.incr("hit_counter")

#push vs set, push tells key must be in the dictionary
r_server.rpush("member", "richard")
r_server.rpush("member", "chuanrui")

#Array reply: list of elements in the specified range.
r_server.lrange("member", 0, -1) 
#print ["richard", "chuanrui"] 
#-1 represent for the ending point

r_server.lrange("member", 0, 0) 
#print ["richard"]

#The number of elements added to the sorted sets, not including elements already existing for which the score was updated
r_server.rpush("member", ("storyid: 3123", 34))
r_server.rpush("member", ("storyid: 9001", 3))

r_server.lrange("member", 0, -1) 
#print [("storyid: 9001", 3), ("storyid: 3123", 34)]

#http://www.w3resource.com/redis/redis-zincrby-key-increment-member.php
r_server.sdd("facebook", 1)
r_server.zincrby("facebook", 2)
# rr_server.get("facebook") => 3


#Lecture 15
class Point(object):
    pass
#object is base class

black = Point()
print Point
#<class '__main__.Point'> 
print black
#<__main__.Point object at 0x7fd487e16350> 
print type(black)
#<class '__main__.Point'> 

#every class has its hashtable, every hashtable linked with one obj with its attributes
black.x = 3
black.y = 4
print black.x

#obj of obj
class Rectangle(object):
    pass
box = Rectangle()
box.width = 100
box.length = 200
box.corner = Point()
box.corner.x = 1
box.corner.y = 1


#shallow copy -> one level
p1 = Point()
p1.x, p1.y = 1, 2

import copy
p2 = copy.copy(p1)
p2.x = 10
print p2.x, p1.x

#Lecture 16
class Time(object):
    def __init__(self, hour=0, minute=0, sec=0):
        self.hour = hour
        self.minute = minute
        self.sec = sec
    
    def __add__(self, other):
        if not isinstance(other, Time):
            print "error"
            return 
        else:
            return self.hour + other.hour, self.minute + other.minute, self.sec + other.sec
    
    def __radd__(self, other):
        if not isinstance(other, Time):
            print "error"
            return 
        else:
            return self.hour + other.hour, self.minute + other.minute, self.sec + other.sec
        
time = Time(1, 2)
print time.hour, time.minute, time.sec
time1 = Time(4)
print time1.hour, time1.minute, time1.sec

#add
result = time + 1
result = time + time1
#radd
result = 1 + time 
print result

"""
#Lecture 17
two = 2
print type(two), type(type(two)), type(two).__bases__
#<type 'int'> <type 'type'> (<type 'object'>,) 


print type(object), type(type)
#<type 'type'> <type 'type'> 

print object.__base__, type.__class__, type.__base__
#None <type 'type'> <type 'object'> 

print isinstance(object, object), isinstance(type, object)
#True True 

#the graph around the inheritance.

