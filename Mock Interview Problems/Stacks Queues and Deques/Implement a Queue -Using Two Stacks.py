'''
Given the Stack class below, implement a Queue class using two stacks! Note, 
this is a "classic" interview problem. Use a Python list data structure as your Stack.
'''

# Solution 1
class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
        
    def dequeue(self):
        # for loop will not be run if stack1 is empty
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
# Solution 2
class Queue2Stacks(object):
    
    def __init__(self):
        # two stacks
        self.instack = []
        self.outstack = []
        
    def enqueue(self,element):
        self.instack.append(element)
        
    def dequeue(self):
        
        # if outstack is empty
        if not self.outstack:
            # while the instack is not empty
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()
