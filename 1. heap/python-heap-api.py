# To make heap in python, can use heapq (unsynchronized) or Queue.PriorityQueue (synchronized)

# 1. Using heapq module

heapq.heapify(x)
# Transform list x into a heap, in-place, in linear time.
# Examples:
from heapq import heapify
ll = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(ll)
print ll # -> [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant.
Example:
from heapq import heapify, heappush
ll = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 1000]
heapify(ll)
print ll # --> [0, 1, 2, 6, 3, 5, 4, 7, 8, 9, 1000]
heappush(ll, 99)
print ll # --> [0, 1, 2, 6, 3, 5, 4, 7, 8, 9, 1000, 99]

heapq.heappop(heap)
# Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
# Example: 
# smallest_three_elements = [heappop(ll) for x in range(3)]

heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# Example: 
from heapq import heapify, heappushpop
ll = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
min = heappushpop(ll, 10) # put 10, pop the min

heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.
# This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

# Difference between heappushpop and heapreplace:
# The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.

# The module also offers three general purpose functions based on heaps.

heapq.merge(*iterables)
# Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
# Example:
from heapq import heapify, merge
heap1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap2 = [11, 0, 5, 7, 19, 20, -2, -1, 18]
heapify(heap1)
heapify(heap2)
print heap1 # -> [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
print heap2 # -> [-2, -1, 5, 0, 19, 20, 11, 7, 18]
# merge heap2 to heap1 (merge returns an iterator, so need to iterate to )
merged = [item for item in merge(heap1, heap2)]
print heap1 # -> [0, 1, 2, 6, 3, 5, 4, 7, 8, 9] (same since merge just copies form original)
print heap2 # -> [-2, -1, 5, 0, 19, 20, 11, 7, 18]
print merged # -> [-2, -1, 0, 1, 2, 5, 0, 6, 3, 5, 4, 7, 8, 9, 19, 20, 11, 7, 18]

# Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).

heapq.nlargest(n, iterable[, key])
# Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
# Example:
from heapq import heapify, nlargest
ls = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
nlargest(2, ls) # -> [9, 8]
# use optional argument 'key' to proved an attribute to sort with
ls2 = [{'key': x, 'data': 'constant'} for x in ls] # -> [{'key:'1', 'data':'constant'}, ...]
nlargest(2, ls2, key=lambda x: x.get('key')) # -> [{'key':9, 'data':'constant'}, {'key':8, 'data': 'constant'}]

heapq.nsmallest(n, iterable[, key])
# Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]
# Usage same as nlargest

# The latter two functions perform best for smaller values of n. For larger values, it is more efficient to use the sorted() function. Also, when n==1, it is more efficient to use the built-in min() and max() functions. If repeated usage of these functions is required, consider turning the iterable into an actual heap.


#examples: sort an interable using heap
>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



Delete an item in the heap
#Example
# Create example data and heapify
a = range(10)
a.reverse()
heapq.heapify(a)
print a

# remove an element and heapify again
a.remove(5)
heapq.heapify(a)
print a

# 2. Queue.PriorityQueue
# not very important
