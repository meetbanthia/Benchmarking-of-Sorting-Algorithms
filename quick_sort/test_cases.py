import random
from quick_sort.quick_sort import quick_sort

def generate_random_list(n):
    list = [random.randint(1, 100) for _ in range(n)]
    random.shuffle(list)
    return list

def generate_sorted_list(n):
    if n == 0:
        return []
    result = [random.randint(1, 100)]
    for i in range(n - 1):
        prev_num = result[-1]
        next_num = random.randint(prev_num + 1, 100)
        result.append(next_num)
    return result

def generate_reverse_sorted_list(n):
    if n == 0:
        return []
    result = [random.randint(1, 100)]
    for i in range(n - 1):
        prev_num = result[-1]
        next_num = random.randint(1, prev_num - 1)
        result.append(next_num)
    return result

def print_list(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate random list")
        print("2. Generate increasing list")
        print("3. Generate decreasing list")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            n = int(input("Enter list size: "))
            arr = generate_random_list(n)
            print("Generated list:")
            print_list(arr)
            quick_sort(arr, 0, n-1)
            print("Sorted list:")
            print_list(arr)
        elif choice == 2:
            n = int(input("Enter list size: "))
            arr = generate_sorted_list(n)
            print("Generated list:")
            print_list(arr)
            quick_sort(arr, 0, n-1)
            print("Sorted list:")
            print_list(arr)
        elif choice == 3:
            n = int(input("Enter list size: "))
            arr = generate_reverse_sorted_list(n)
            print("Generated list:")
            print_list(arr)
            quick_sort(arr, 0, n-1)
            print("Sorted list:")
            print_list(arr)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
