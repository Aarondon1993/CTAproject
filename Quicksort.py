## Quicksort

def QuickSort(n):

    Figures = len(n)
    
    if Figures < 2:
        return n
    
    current_position = 0 

    for i in range(1, Figures): 
         if n[i] <= n[0]:
              current_position += 1
              temp = n[i]
              n[i] = n[current_position]
              n[current_position] = temp

    temp = n[0]
    n[0] = n[current_position] 
    n[current_position] = temp 
    
    left = QuickSort(n[0:current_position]) 
    right = QuickSort(n[current_position+1:Figures]) 

    n = left + [n[current_position]] + right 
    
    return n



array_to_be_sorted = [4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",QuickSort(array_to_be_sorted))