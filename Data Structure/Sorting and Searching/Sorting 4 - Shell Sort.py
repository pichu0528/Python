'''
The shell sort improves on the insertion sort by breaking the original list into a number of smaller 
sublists, each of which is sorted using an insertion sort. The unique way that these sublists are 
chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous items, 
the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all 
items that are i items apart.
'''

def shell_sort(arr):
    
    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        for start in range(sublistcount):
            
            gap_insertion_sort(arr,start,sublistcount)
            
        # visual presentation of the list
        print('After increments of size: ', sublistcount)
        print('The list is ', arr)
            
        sublistcount = sublistcount//2
    
def gap_insertion_sort(arr,start,gap):
    
    for i in range(start+gap,len(arr),gap):
        
        currentvalue = arr[i]
        position = i
        
        while position >= gap and arr[position-gap] > currentvalue:
            
            arr[position] = arr[position-gap]
            position = position - gap
            
        arr[position] = currentvalue
    
