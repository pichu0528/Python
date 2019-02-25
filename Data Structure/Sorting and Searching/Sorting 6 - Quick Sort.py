def quick_sort(arr):
    
    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):
    
    if first < last:
        
        splitpoint = partition(arr,first,last)
        
        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

def partition(arr,first,last):
    
    # use the first item as the pivot point
    pivotvalue = arr[first]
    
    # left mark starts at one index after the pivot point
    # and right mark starts at the end of array
    leftmark = first + 1
    rightmark = last
    
    done = False
    
    while not done:
        
        # moving the leftmark to the right until the value is greater
        # than the pivot value
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
            
        
        # moving the rightmark to the left until the value is less than
        # the pivot value
        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            rightmark -= 1
            
        if rightmark < leftmark:
            done = True
            
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
            
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    
    # return the right mark because that is where the pivot value
    # is in the middle of the partition
    # considering: [3, 2, 2, 4, 4]
    # leftmark will result at index 3
    # rightmark will result at index 2
    # swapping rightmark and the pivot point will be the way to go in
    # this sense.
    return rightmark
