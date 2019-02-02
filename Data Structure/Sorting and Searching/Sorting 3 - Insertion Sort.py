# Solution 1 -
def insertion_sort1(arr):
    
    # mark first element as sorted
    sort = 0
    
    # for each unsorted element
    for i in range(1,len(arr)):
        
        # extract the element
        temp = arr[i]

        # for i = lastsortedIndex to 0
        for j in range(sort,-1,-1):
            
            # if currentSortedElement > extractedElement
            if arr[j] > temp:
                
                # move sorted element to the right by 1
                arr[j+1] = arr[j]
                # if j equals 0, we know that we only have one slot left
                # put the temp value at the last slot
                if j == 0:
                    
                    arr[j] = temp
            
            # else insert extracted element and break
            else:
                
                arr[j+1] = temp
                break

        sort += 1
        print(arr)
                
    return arr
    
    
# Solution 2 
def insertion_sort2(arr):
    
    # For every index in array
    for i in range(1,len(arr)):
        
        # Set current values and position
        currentvalue = arr[i]
        position = i
        
        # Sorted Sublist
        while position>0 and arr[position-1]>currentvalue:
            
            arr[position]=arr[position-1]
            position = position-1

        
        arr[position]=currentvalue
        print(arr)
