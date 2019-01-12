'''
Write a function to reverse a Linked List in place. The function will take in the head of the list 
as input and return the new head of the list.

You are given the example Linked List Node class:
class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
'''

# Solution - Space complexity: O(1)
#            Time complexity: O(N)
#            We can reverse the list by changing the next pointer of each node. Each node's next 
#            pointer should point to the previous node.
def reverse(head):
    
    # for ex: a -> b -> c -> d
    current_node = head
    prev_node = None
    next_node = None
    
    # until we have gone through to the end of the list
    while current_node:
        
        # make sure to copy the current nodes next node to a variable next_node
        # before overwriting as the previous node for reversal
        next_node = current_node.nextnode
        
        # reverse the current_node pointer to the prev_node
        current_node.nextnode = prev_node
        
        # Go one forward in the list
        prev_node = current_node
        current_node = next_node
    
    return prev_node
