"""
ALGORITHM:
Radix Sort is a non-comparative sorting algorithm that sorts an array by grouping the elements by their individual digits. 
It can sort integers, strings, and other data types that can be represented as a sequence of digits. 
Radix Sort works by sorting the digits starting from the least significant digit to the most significant digit.
"""

def radix_sort(arr):
    max_digit = len(str(max(arr)))

    for i in range(max_digit):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = num // 10 ** i % 10
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]

    return arr
