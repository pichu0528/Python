
# For unordered arr, the time complexity will be O(N)
def seq_search(arr,ele):
    
    pos   = 0
    found = False
    
    while pos < len(arr) and not found:
        
        if arr[pos] == ele:
            found = True
        else:
            pos += 1
            
    return found
    
# For ordered/sorted arr, the time complexity will be O(N). However, the avg time complexity
# is O(n/2).
def ordered_seq_search(arr,ele):
    pos   = 0
    found = False
    stopped = False
    
    while pos < len(arr) and not found and not stopped:
        
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1
            
    return found
