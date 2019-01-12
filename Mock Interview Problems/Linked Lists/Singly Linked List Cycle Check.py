'''
Given a singly linked list, write a function which takes in the first node in a singly linked list
and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is 
also sometimes known as a circularly linked list.

You've been given the Linked List Node class code:

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
'''

# Solution 1 - use a while loop to compare the initial node and the next nodes.
#              This solution is only suitable to find the perfect circularly linked list.
def cycle_check1(node):
    initial_node = node

    while node.nextnode != None:
        if initial_node != node.nextnode:
            node = node.nextnode
        else:
            return True
        
    return False
    
# Solution 2 - use two variable. One travels faster, and the other travels slower.
#              If both values ever overlap, then we know there is a cycle.
def cycle_check2(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        
        if marker2 == marker1:
            return True
        
    return False
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check1)
t.test(cycle_check2)
