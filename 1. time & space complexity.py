
Lists:
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | l[i]         | O(1)         |
Store         | l[i] = 0     | O(1)         |
Length        | len(l)       | O(1)         |
Append        | l.append(5)  | O(1)         |
Pop           | l.pop()      | O(1)         | same as l.pop(-1), popping at end
Clear         | l.clear()    | O(1)         | similar to l = []

Slice         | l[a:b]       | O(b-a)       | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
Extend        | l.extend(...)| O(len(...))  | depends only on len of extension
Construction  | list(...)    | O(len(...))  | depends on length of ...

check ==, !=  | l1 == l2     | O(N)         |
Insert        | l[a:b] = ... | O(N)         |
Delete        | del l[i]     | O(N)         | 
Remove        | l.remove(...)| O(N)         | 
Containment   | x in/not in l| O(N)         | searches list
Copy          | l.copy()     | O(N)         | Same as l[:] which is O(N)
Pop           | l.pop(i)     | O(N)         | O(N-i): l.pop(0):O(N)
Extreme value | min(l)/max(l)| O(N)         |
Reverse       | l.reverse()  | O(N)         |
Iteration     | for v in l:  | O(N)         |

Sort          | l.sort()     | O(N Log N)   | key/reverse doesn't change this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
Multiply      | k*l          | O(k N)       | 5*l is O(N): len(l)*l is O(N**2)

Tuples support all operations that do not mutate the data structure (and with
the same complexity classes).

Stack & Queue are similar to the list.

Sets:
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Length        | len(s)       | O(1)          |
Add           | s.add(5)     | O(1)          |
Containment   | x in/not in s| O(1)          | compare to list/tuple - O(N)
Remove        | s.remove(5)  | O(1)          | compare to list/tuple - O(N)
Discard       | s.discard(5) | O(1)          | 
Pop           | s.pop(i)     | O(1)          | compare to list - O(N)
Clear         | s.clear()    | O(1)          | similar to s = set()

Construction  | set(...)     | O(len(...))   | depends on length of ...
check ==, !=  | s != t       | O((len(s))    | same as len(t): if different, False
<=/<          | s <= t       | O(len(s))     | issubset
>=/>          | s >= t       | O(len(t))     | issuperset s <= t == t >= s
Union         | s | t        | O(len(s)+len(t))
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))

Iteration     | for v in s:  | O(N)          |
Copy          | s.copy()     | O(N)          |

Sets have many more operations that are O(1) compared with lists and tuples.
Not needing to keep values in a specific order (which lists/tuples require)
allows for faster operations.

Frozen sets support all operations that do not mutate the data structure (and
with the same complexity classes).


Heap -> min-heap in this case

Operation     | Example                           | Class            | Notes
--------------+-----------------------------------+------------------+-------------------------------
find-min	  | h[0]                              | O(1)             |
merge         | merged = [item for item in merge(heap1, heap2)]| O(n)|
build heap    | ---------                         | O(n)             |   
replace       | heapq.heapreplace(heap, item)     | O(log n)         | heapq.heappushpop(heap, item)
Delete        | h.remove(5)                       | O(log n)         |
insert        | heappush(ll, 99)                  | O(log n)         |
heapsort      | heapsort                          | O(nlog n)        | 



Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items



Dictionaries: dict and defaultdict
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | d[k]         | O(1)          |
Store         | d[k] = v     | O(1)          |
Length        | len(d)       | O(1)          |
Delete        | del d[k]     | O(1)          |
get/setdefault| d.method     | O(1)          |
Pop           | d.pop(k)     | O(1)          |
Pop item      | d.popitem()  | O(1)          |
Clear         | d.clear()    | O(1)          | similar to s = {} or = dict()
Views         | d.keys()     | O(1)          |

Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items

So, most dict operations are O(1).


linked list 
			ion	
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Access        | ---          | O(n)          |
Search        | ---          | O(n)          |
Insert        | ---          | O(1)          |
Delete        | ---          | O(1)          |










