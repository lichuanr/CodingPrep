# different ways of constructing dict
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> f = {x[0]: x[1] for x in [('two', 2), ('one', 1), ('three', 3)]}
>>> a == b == c == d == e == f
True

# different ways of accessing dictionary values
>>> a.get('two') == a['two']

# different was of insert key-value to dictionary
>>> a['four'] = 4
>>> a.update([('four', 4,)])

# update multiple items
dict.update()
>>> a.update([ (str(x), x) for x in range(10)])

len(dict)
# get the number of items in dict
>>> len(dict([('1', 1), ('2', 2), ('3', 3)]))
3

dict.pop(key[, default])
# If key is in the dictionary, remove it and return its value, else return default. 
# If default is not given and key is not in the dictionary, a KeyError is raised.
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d.pop('one', None)
1
>>> d.pop('ten', None)
>>> print d.pop('ten', None)
None
>>> d.pop('ten')
KeyError

dict.popitem()
# remove and return arbitrary item from dict. Useful to destructively iterate over dict

dict.has_key(key)
# returns True if dict has that key
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d.has_key('one')
True
>>> d.has_key('ten')
False

dict.values()
# returns a list of dictionary values
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d.values()
[1, 2, 3]

dict.keys()
# returns a list of keys
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d.keys()
['one', 'two', 'three']

dict.items()
# returns a list of dictionary items as a list of (key, val) tuples
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d.items()
[('one', 1), ('two', 2), ('three', 3)]

dict.viewkeys(), dict.viewvalues(), dict.viewitems()
# They provide a dynamic view on the dictionary’s entries, which means
# that when the dictionary changes, the view reflects these changes.

# dictviews are set-like since their entries are unique and hashable.
# Therefore they have set operations:
dictview & other
# Return the intersection of the dictview and the other object as a new set.
dictview | other
# Return the union of the dictview and the other object as a new set.
dictview - other
# Return the difference between the dictview and the other object (all elements 
# in dictview that aren’t in other) as a new set.
dictview ^ other
# Return the symmetric difference (all elements either in dictview or other, 
# but not in both) of the dictview and the other object as a new set.
# Examples:
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d2 = {'one': 1, 'two': 2, 'four': 4}
>>> d.viewitems() & d2.viewitems()
set([('two', 2), ('one', 1)])
>>> d.viewitems() - d2.viewitems()
set([('three', 3)])
>>> d.viewitems() | d2.viewitems()
set([('one', 1), ('two', 2), ('four', 4), ('three', 3)])

# if __name__=="__main__":
# 	a = dict(one=1, two=2, three=3)
# 	b = {'one': 1, 'two': 2, 'three': 3}
# 	c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# 	d = dict([('two', 2), ('one', 1), ('three', 3)])
# 	e = dict({'three': 3, 'one': 1, 'two': 2})
# 	f = {x[0]: x[1] for x in [('two', 2), ('one', 1), ('three', 3)]}
# 	print (a == b == c == d == e == f)
# 	# True