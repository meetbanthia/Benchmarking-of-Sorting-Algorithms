"""
ALGORITHM:
Radix Sort is a non-comparative sorting algorithm that sorts an array by grouping the elements by their individual digits. 
It can sort integers, strings, and other data types that can be represented as a sequence of digits. 
Radix Sort works by sorting the digits starting from the least significant digit to the most significant digit.
"""

# best -> sorted
# avg -> random
# worst -> reverse sorted

def countingSort(arr, exp1):
 
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
