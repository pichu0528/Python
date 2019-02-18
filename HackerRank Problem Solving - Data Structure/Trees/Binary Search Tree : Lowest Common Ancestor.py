### [Challenge Name: Binary Search Tree : Lowest Common Ancestor]
### (/challenges/binary-search-tree-lowest-common-ancestor)

'''
You are given pointer to the root of the binary search tree and two values $v1$ and $v2$. 
You need to return the lowest common ancestor of $v1$ and $v2$ in the binary search tree.  

    2
   / \
  1   3
     / \
    4   5
         \
          6

In the diagram above, the lowest common ancestor of the nodes $4$ and $6$ is the node $3$.  
Node $3$ is the lowest node which has nodes $4$ and $6$ as descendants.

**Function Description**  

Complete the function *lca* in the editor below.  
It should return a pointer to the lowest common ancestor node of the two values given.  

lca has the following parameters:  
-  root: a pointer to the root node of a binary search tree  
-  v1: a node.data value  
-  v2: a node.data value 
'''


'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here

    if v1 > root.info and v2 > root.info:
        common = lca(root.right,v1,v2)
    elif v1 < root.info and v2 < root.info:
        common = lca(root.left,v1,v2)
    else:
        common = root

    return common
