# Solution 1 - looking for min
def selection_sort1(arr):
    
    unsorted_index = 0
    
    for _ in range(len(arr)-1):
        minimum = arr[unsorted_index]
        m_index = unsorted_index
        for i in range(unsorted_index+1,len(arr)):
            if minimum > arr[i]:
                minimum = arr[i]
                m_index = i
                
        temp = arr[unsorted_index]
        arr[unsorted_index] = minimum
        arr[m_index] = temp
        unsorted_index += 1
        print(arr)
        
# Solution 2 - looking for max
def selection_sort2(arr):
    
    # For every slot in array
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax=0
        
        # For every set of 0 to fillslot+1
        for location in range(1,fillslot+1):
            # Set maximum's location
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
        print(arr)
