##Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
             if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


                        
arr= [50,11,213,1235,151,484,989,1,35,78,45]

bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])    


## Code obtained from https://www.geeksforgeeks.org/python-program-for-bubble-sort/                   