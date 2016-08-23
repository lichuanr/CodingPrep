#define a linked list
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

head = ListNode(1, ListNode(3, ListNode(3, ListNode(1, ListNode(1)))))



#Backward print the linked list
def print_backward(list):
    if list == None: return
    head = list
    tail = list.next
    print_backward(tail)
    print head,

>>> print_backward(node1)
3 2 1