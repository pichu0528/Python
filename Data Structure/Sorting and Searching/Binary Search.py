'''
Not using recursion
'''
def binary_search(arr,ele):
    
    first = 0
    last = len(arr) - 1
    
    found = False
    
    while first <= last and not found:
        
        mid = (first+last)//2
        
        if arr[mid] == ele:
            found = True
        
        else:
            if arr[mid] > ele:
                last = mid - 1
            else:
                first = mid + 1
            
    return found
    
'''
Using Recursion
'''
def binary_search_recur(arr,ele):
    
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    
    if arr[mid] == ele:
        return True
    else:
        if arr[mid] > ele:
            return binary_search_recur(arr[:mid],ele)
        else:
            return binary_search_recur(arr[mid+1],ele)
