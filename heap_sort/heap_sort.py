def heap_sort(arr):
    n = len(arr)
    comparisons = 0

    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        comparisons += heapify(arr, i, 0)

    return arr, comparisons

def heapify(arr, n, i):
    comparisons = 0
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += 1
        comparisons += heapify(arr, n, largest)

    return comparisons
