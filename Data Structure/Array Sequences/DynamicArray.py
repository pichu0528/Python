import ctypes

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0 # start at size 0
        self.capacity = 1 # start at capacity 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        # If k is not within 0 and size n, 
        # throw IndexError
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        
        return self.A[k]
    
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough
        self.A[self.n] = ele # assign the element to index n
        self.n += 1 # increment size n for next ele
    
    def _resize(self,new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        
        return (new_cap * ctypes.py_object)()
