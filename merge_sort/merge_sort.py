"""
ALGORITHM:
Merge Sort is a divide and conquer algorithm that divides the array into two halves, 
sorts them recursively, and then merges the two sorted halves into a single sorted array.
"""

# best -> sorted
# avg -> random
# worst -> reverse sorted

def merge_sort(arr):
    count = 0  # initialize count
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        count += merge_sort(left_arr)  # add to count recursively
        count += merge_sort(right_arr)  # add to count recursively
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            count += 1  # increment count for each comparison
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return count  # return the total count

