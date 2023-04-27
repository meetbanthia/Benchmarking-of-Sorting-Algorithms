"""
ALGORITHM:
Heap Sort is a sorting algorithm that sorts an array by first converting it into a binary heap.
The binary heap is then sorted by repeatedly removing the largest element and placing it at the end of the array. 
The process is repeated until the heap is empty.
"""
# best -> sorted
# average -> random
# worst -> reverse sorted

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    # node values in the tree
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively call the function
        heapify(arr, n, largest)