# Solution 1
def bubble_sort1(arr):
    
    n = len(arr)
    
    for _ in range(0,n):
        for j in range(1,n):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
        
    return arr
    
# Solution 2
def bubble_sort2(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        #
        for k in range(n):
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr
