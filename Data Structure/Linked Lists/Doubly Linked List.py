class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None
        
# initialize three nodes for example        
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# set up next_node and prev_node
a.next_node = b
b.next_node = c

b.prev_node = a
c.prev_node = b
