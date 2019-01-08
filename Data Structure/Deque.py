'''
- Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
- addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
- addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
- removeFront() removes the front item from the deque. It needs no parameters and returns the item. 
  The deque is modified.
- removeRear() removes the rear item from the deque. It needs no parameters and returns the item. 
  The deque is modified.
- isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean 
  value.
- size() returns the number of items in the deque. It needs no parameters and returns an integer.
'''

# 1 - Front|item|item|item|item|Rear
class Deque(object):
    
    def __init__(self):
        self.items = []
    
    def addFront(self,item):
        self.items.insert(0,item)
    
    def addRear(self,item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
        
# 2 - Rear|item|item|item|item|Front
class Deque(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
