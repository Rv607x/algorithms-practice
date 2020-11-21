# Quick sort is a divide and conquer type of Algorithm where you break down the problem in smaller chunks
# Solve the individal problems then combine for the solution
# in this case we select a pivot and other 2 groups; less and greater
# less are the values less than pivot while greater > pivot.
# recursively solve both then add them up together 

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([3, 99, 6, 9, 44, 60, 2, 1000, 4, 1]))