class HashTable(object):
    
    # Set up size and slots and data
    def __init__(self,size):
        self.size  = size
        self.slots = [None] * self.size
        self.data  = [None] * self.size
        
    def put(self,key,data):
        # Note: we will only use integer keys for ease of use with the Hash Function
        
        # Get the hash value
        hashvalue = self.hashfunction(key,len(self.slots))
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            
        else:
            
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    
    # Using the remainder method
    def hashfunction(self,key,size):
        # The actual hash function
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def get(self,key):
        
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
                    
        return data
    
    # Special method for Python indexing
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
