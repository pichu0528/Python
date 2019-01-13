'''
Write a function that takes a head node and an integer value n and then returns the nth to last 
node in the linked list. For example, given:

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None
        
Example Input and Output:
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
target_node.value
4
'''

# Solution 1 - Space complexity: O(1)
#              Time complexity : O(N)
def nth_to_last_node1(n, head):
    
    # figure out how many nodes there are
    # time complexity: O(N)
    temp = head
    count = 1
    while temp.nextnode != None:
        count += 1
        temp = temp.nextnode
    
    # nth to the last meaning total # of nodes - n
    # note: index start at 0
    target_count = count - n
    target = head
    
    # find the target node by looping until we get 
    # to the target_count
    # time complexity: O(N)
    for _ in range(target_count):
        target = target.nextnode
    return target

# Solution 2 - have two pointers, left and right pointers, with n distance between them.
#              Increment both pointers until the right pointer reach the end.
#              Then, return the left pointer.
#              Space complexity: O(1)
#              Time complexity : O(N)
def nth_to_last_node2(n,head):
    left_pointer = head
    right_pointer = head
    
    for _ in range(n-1):
        
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')
            
        right_pointer = right_pointer.nextnode
        
    while right_pointer.nextnode:
        
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
        
    return left_pointer

"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print 'ALL TEST CASES PASSED'
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node1)
t.test(nth_to_last_node2)
