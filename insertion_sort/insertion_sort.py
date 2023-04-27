"""
ALGORITHM:
Insertion Sort is a simple sorting algorithm that works by repeatedly iterating through an array 
and sorting each element at its correct position with respect to the already sorted elements.
"""

# best -> sorted
# avg -> random
# worst -> reverse sorted

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1 
        arr[j + 1] = key

