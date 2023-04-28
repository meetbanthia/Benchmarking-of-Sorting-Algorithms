"""
ALGORITHM:
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element 
as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position 
in the sorted array.
"""

# best -> pivot at middle -> sorted with pivot choice 3
# avg -> jumbled woth pivot choice = 2
# worst -> pivot at start or end -> random array with pivot choice = 1

import random

def quick_sort_version1(arr, low, high):
    count = 0
    if low < high:
        pivot = arr[low]
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version1(arr, low, pivot_idx - 1)
        quick_sort_version1(arr, pivot_idx + 1, high)
    return count

def quick_sort_version2(arr, low, high):
    if low < high:
        pivot = random.choice(arr[low:high+1])
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version2(arr, low, pivot_idx - 1)
        quick_sort_version2(arr, pivot_idx + 1, high)

def quick_sort_version3(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        candidates = [arr[low], arr[mid], arr[high]]
        candidates.remove(max(candidates))
        candidates.remove(min(candidates))
        pivot = candidates[0]
        pivot_idx = partition(arr, low, high, pivot)
        quick_sort_version3(arr, low, pivot_idx - 1)
        quick_sort_version3(arr, pivot_idx + 1, high)


def partition(arr, low, high, pivot):
    pivot_idx = arr.index(pivot)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

