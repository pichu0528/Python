'''
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the 
numbers in the new tree are between min and max (inclusive). The resulting tree should still be a
valid binary search tree.
'''

# Solution 1 - use the post-order traversal idea
def trimBST(tree, minVal, maxVal):
  if not tree:
    return
  
  tree.left  = trimBST(tree.left, minVal, maxVal)
  tree.right = trimBST(tree.right, minVal, maxVal)
  
  if minVal <= tree.val <= maxVal:
    return tree
  elif tree.val < minVal:
    return tree.right
  elif tree.val > maxVal:
    return tree.left
