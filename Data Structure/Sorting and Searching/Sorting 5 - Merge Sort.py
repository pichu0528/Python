def merge_sort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i, j, k = 0, 0, 0
        
        # comparing two list and merge them back to arr
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
                
            k += 1
        
        # if there is anything left in the lefthalf, place the values to the end
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        # if there is anything left in the righthalf, place the values to the end
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1          
