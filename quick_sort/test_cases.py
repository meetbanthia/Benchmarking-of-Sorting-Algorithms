import random
import time
from quick_sort import quick_sort

def generate_random_list(n):
    list = [random.randint(1, 1000000) for _ in range(n)]
    random.shuffle(list)
    return list

def generate_sorted_list(n):
    list = []
    last_num = 0
    for i in range(n):
        new_num = random.randint(last_num+1, last_num+10)
        list.append(new_num)
        last_num = new_num
    return list

def generate_reverse_sorted_list(n):
    list = []
    last_num = 100
    for i in range(n):
        new_num = random.randint(last_num-10, last_num-1)
        list.append(new_num)
        last_num = new_num
    return list

def print_list(arr):
    print("The list is: [", end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")

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

def main():
    while True:
        print("Choose an option:")
        print("1. Sort a randomly generated list")
        print("2. Sort a list sorted in increasing order")
        print("3. Sort a list sorted in decreasing order")
        option = input("Enter your choice: ")
        if option not in ["1", "2", "3"]:
            print("Invalid option")
            continue
        n = int(input("Enter the size of the list: "))
        if option == "1":
            arr = generate_random_list(n)
            print_list(arr)
        elif option == "2":
            arr = generate_sorted_list(n)
            print_list(arr)
        else:
            arr = generate_reverse_sorted_list(n)
            print_list(arr)
        
        import random
import time
from quick_sort import quick_sort

def generate_random_list(n):
    list = [random.randint(1, 1000000) for _ in range(n)]
    random.shuffle(list)
    return list

def generate_sorted_list(n):
    list = []
    last_num = 0
    for i in range(n):
        new_num = random.randint(last_num+1, last_num+10)
        list.append(new_num)
        last_num = new_num
    return list

def generate_reverse_sorted_list(n):
    list = []
    last_num = 100
    for i in range(n):
        new_num = random.randint(last_num-10, last_num-1)
        list.append(new_num)
        last_num = new_num
    return list

def print_list(arr):
    print("The list is: [", end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")

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

def main():
    while True:
        print("Choose an option:")
        print("1. Sort a randomly generated list")
        print("2. Sort a list sorted in increasing order")
        print("3. Sort a list sorted in decreasing order")
        option = input("Enter your choice: ")
        if option not in ["1", "2", "3"]:
            print("Invalid option")
            continue
        n = int(input("Enter the size of the list: "))
        if option == "1":
            arr = generate_random_list(n)
            print_list(arr)
        elif option == "2":
            arr = generate_sorted_list(n)
            print_list(arr)
        else:
            arr = generate_reverse_sorted_list(n)
            print_list(arr)
        
        with open("time_data.csv", "a") as f:
            f.write("Pivot choice\tTime taken (seconds)\n")
            for pivot_choice in range(1, 4):
                f.write(f"{pivot_choice}\t")
                pivot = choose_pivot(arr, pivot_choice)
                start_time = time.time()
                sorted_arr = quick_sort(arr, 0, len(arr) - 1, pivot)
                end_time = time.time()
                f.write(f"{end_time - start_time:.5f}\n")
                print("Pivot choice:", pivot_choice)
                print("Sorted list:", sorted_arr)
                print("Time taken:", end_time - start_time, "seconds")
                print()
        
        break

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()

