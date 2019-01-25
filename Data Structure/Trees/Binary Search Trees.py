class TreeNode:
    
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key        = key
        self.payload    = val
        self.leftChild  = left
        self.rightChild = right
        self.parent     = parent
        
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key        = key
        self.payload    = value
        self.rightChild = rc
        self.leftChild  = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
            
        if self.hasRightChild():
            self.rightChild.parent = self
            
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
                
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent
    
    # find the next-largest key in the tree, aka successor
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
        
 '''
A binary search tree relies on the property that keys that are less than the 
parent are found in the let subtree, and keys that are greater than the parent
are found in the right subtree. (BST property)

The code below uses Map interface for implementation

All the keys in the left subtree are less than the key in the root.
All the keys in the right subtree are greater than the root.

The BinarySearchTree class has a reference to the TreeNode that is the root 
of the binary search tree.

put method
This method will check if the tree already has a root.
If there is not a root then put will create a new TreeNode and install it 
as the root of the tree.
If a root node already exists, then put calls the private, recursive, helper
function _put to search the tree according to the following algorithm:
1. Starting at the root of the tree, search the binary tree comparing the 
   new key to the key in the current node.
2. If the new key is less than the current node, search the left subtree.
   If the new key is greater than the current node, search the right subtree.
3. When there is no left (or right) child to search, we have found the 
   position in the tree where the new node should be installed.
4. To add a node to the tree, create a new TreeNode object and insert the 
   object at the point discovered in the prevoius step.
   
get method
It simply searches the tree recursively until it gets a non-matching leaf node
or finds a matching key.
When a matching key is found, the value stored in the payload of the node is
returned.
Using get, we can implement the in operation by writing a __contains__ method
for the BinarySearchTree.
The __contains__ method will simply call get and return True if get returns
a value, or False if it returns None.

The most challenging method in the binary search tree is the deletion of a key.
The first task is to find the node to delete by searching the tree.
If the tree has more than one node we search using the _get method to find the 
TreeNode that needs to be removed.
If the tree only has a single node, that means we are removing the root of the
treee, but we still must check to make sure the key of the root matches the key
that is to be deleted.
In either case if the key is not found the del operator raises an error.
Once we've found the node containing the key we want to delete, there are three
cases that we must consider:
1. The node to be deleted has no children.
    - If the current node has no children all we need to do is delete the node
      and remove the reference to this node in the parent.
2. The node to be deleted has only one child.
    - If a node has only a single child, then we can simply promote the child
      to take the place of its parent.
3. The node to be deleted has two children - most difficult to handle.
    - If a node has two children, then it is unlikely that we can simply
      promote one of them to take the node's place.
      We can, however, search the tree for a node that can be used to replace
      the one scheduled for deletion.
    - What we need is a node that will preserve the binary search tree 
      relationships for both of the existing left and right subtrees.
    - The node that will do this is the node that has the next-largest key in
      the tree. We call this node the successor.
    - The successor is guaranteed to have no more than one child, so we know
      how to remove it using the two cases for deletion that we have already
      implemented.
    - Once the successor has been removed, we simply put it in the tree in
      place of the node to be deleted.
    - Notice that we make use of the helper methods findSuccessor and findMin
      to find the successor.
    - To remove the successor, we make use of the method spliceOut.
    - The reason we use spliceOut is that it goes directly to the node we want
      to splice out and makes the right changes.
'''
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    # where to put the new key with the new value
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
        
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                
    def __setitem__(self,k,v):
        self.put(k,v)
        
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
        
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')
    
    # special method: allow to use the del method
    def __delitem__(self,key):
        self.delete(key)
    
    def remove(self,currentNode):
        # If the current node has no children all we need to do is delete the node
        # and remove the reference to this node in the parent.
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
                
        
        elif currentNode.hasBothChildren(): #interior
            
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            
        
        # If a node has only a single child, then we can simply promote the child
        # to take the place of its parent.
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
