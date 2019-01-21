class BinaryTree(object):
    
    def __init__(self,rootObj):
        
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            
        else:
            t = BinaryTree(newNode)
            # pushing the original left child down 
            # one level
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        
        if self.rightChild == None:
            self.rightChild = newNode
        else:
            t = BinaryTree(newNode)
            # pushing the original right child down
            # one level
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        
        return self.rightChild
    
    def getLeftChild(self):
        
        return self.leftChild
    
    def setRootVal(self, obj):
        
        self.key = obj
        
    def getRootVal(self):
        
        return self.key
