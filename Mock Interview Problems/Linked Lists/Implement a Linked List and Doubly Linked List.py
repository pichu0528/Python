'''
For this interview problem, implement a node class and show how it can be used to create 
a singly linked list and a doubly linked list.
'''

class SinglyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        self.prevnode = None
        
# Singly Linked List Initialization
a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)

a.nextnode = b
b.nextnode = c

# Doubly Linked List Initialization
x = DoublyLinkedListNode(4)
y = DoublyLinkedListNode(5)
z = DoublyLinkedListNode(6)

x.nextnode = y
y.nextnode = z

y.prevnode = x
z.prevnode = y
