# selection sort algorithm in python
# to sort we first find the smallest element then 
# use the smallest element to sort the array

def findSmallest(arr):
    """ function to find the index of the smallest
     element of an array"""

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """ sorting by using the smallest value. 
    creates a new array then loops through the array and adds the 
    small value to the new array. Then deletes it after addition
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# test values to sort
print(selectionSort([58, 11, 35, 8, 2, 1098, 34, 9]))