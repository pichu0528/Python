'''
Given a binary tree of integers, print it in level order. The output will contain space between 
the numbers in the same level, and new line between different levels. For example, if the tree is:

        1
    2       3
 4        5   6
 
The output should be:
1 
2 3 
4 5 6
'''
# Given the following node class
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val

# Solution 1 - use a list that behaves like a queue to keep track of the nodes.
               Use currentcount and nextcount to represent how many nodes are in the current level
               and the next level, so we can determine when to insert a new line.
               Using BFS property to solve this problem.

def levelOrderPrint1(tree):
    
    q = []
    q.append(tree)
    currentcount, nextcount = 1,0
    
    while len(q) > 0:
        temp = q.pop(0)
        print(temp.val,end=' ')
        currentcount -= 1
        if temp.left:
            q.append(temp.left)
            nextcount += 1
        if temp.right:
            q.append(temp.right)
            nextcount += 1
        # when currentcount equals to 0, we know that we have printed all the current level
        # nodes. So, we need reassign the currentcount to nextcount for next level nodes
        if currentcount == 0:
            print('\n', end='')
            currentcount, nextcount = nextcount, currentcount
            
# Solution 2 - similar idea as the solution 1, but using deque from collections as the 
               container for the nodes

import collections

def levelOrderPrint2(tree):
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        print(currentNode.val,end=' '),
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount+=1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount+=1
        if currentCount==0:
            #finished printing current level
            print('\n', end='')
            currentCount, nextCount = nextCount, currentCount        
            
# Test your code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

levelOrderPrint1(root)
levelOrderPrint2(root)
