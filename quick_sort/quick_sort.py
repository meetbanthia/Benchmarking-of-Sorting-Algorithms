"""
ALGORITHM:
Heap Sort is a sorting algorithm that sorts an array by first converting it into a binary heap. 
The binary heap is then sorted by repeatedly removing the largest element and placing it at the end of the array. 
The process is repeated until the heap is empty.
"""

# best -> pivot at middle -> sorted with pivot choce 3
# avg -> jumbled woth pivot choice = 2
# worst -> pivot at start or end -> random array with pivot choice = 1

import random

def quick_sort(arr, low, high, pivot_choice):
    if low < high:
        if pivot_choice == 1:
            pivot = arr[low]
        elif pivot_choice == 2:
            pivot = random.choice(arr[low:high+1])
        else:
            mid = (low + high) // 2
            candidates = [arr[low], arr[mid], arr[high]]
            candidates.remove(max(candidates))
            candidates.remove(min(candidates))
            pivot = candidates[0]
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort(arr, low, pivot_idx - 1, pivot_choice)
        quick_sort(arr, pivot_idx + 1, high, pivot_choice)
    return arr

def partition(arr, low, high, pivot):
    pivot_idx = arr.index(pivot)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



