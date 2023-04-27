import random

def choose_pivot(arr, pivot_choice):
    if pivot_choice == 1:
        return arr[0]
    elif pivot_choice == 2:
        return random.choice(arr)
    elif pivot_choice == 3:
        first = arr[0]
        middle = arr[len(arr)//2]
        last = arr[-1]
        if first <= middle <= last or last <= middle <= first:
            return middle
        elif middle <= first <= last or last <= first <= middle:
            return first
        else:
            return last