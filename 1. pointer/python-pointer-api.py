They are not quite pointers, they are references to objects. Objects can be either mutable, or immutable.
An immutable object is copied when it is modified. A mutable object is altered in-place. An integer is an immutable object, 
that you reference by your i and j variables. A list is a mutable object.

In your first example

i=5
# The label i now references 5
j=i
# The label j now references what i references
j=3
# The label j now references 3
print i
# i still references 5

In your second example:

i=[1,2,3]
# i references a list object (a mutable object)
j=i
# j now references the same object as i (they reference the same mutable object)
i[0]=5
# sets first element of references object to 5
print j
# prints the list object that j references. It's the same one as i.