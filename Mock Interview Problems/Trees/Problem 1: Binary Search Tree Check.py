'''
If a tree is a binary search tree, then traversing the three
in order should lead to sorted order of the values in the tree.
So, we can perform an inorder traversal and check whether the 
node values are sorted or not.
'''
l = []
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        l.append(tree.getRootVal())
        inorder(tree.getRightChild())
    return l

def solution(tree):
    temp = inorder(tree)
    i = 0
    return temp == sorted(temp)
#     while i < len(temp):
#         if i+1 < len(temp):
#             if temp[i] < temp[i+1]:
#                 i += 1
#                 continue
#             else:
#                 return False
#         return True
