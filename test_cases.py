import random
import time
from quick_sort.quick_sort import quick_sort
from quick_sort.pivot import choose_pivot
from heap_sort.heap_sort import heap_sort
from merge_sort.merge_sort import merge_sort
from radix_sort.radix_sort import radix_sort
from insertion_sort.insertion_sort import insertion_sort
import sys
sys.setrecursionlimit(10**6)

# Three types of functions to generate three different types of lists
def generate_random_list(n):
    list = [random.randint(1, 1000) for _ in range(n)]
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

def main():
    # Boolean value
    temp1=True
    for n in range(100,1001,100):
        arr = generate_sorted_list(n)
        with open("quick_sort/time_data_qs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")
                pivot = choose_pivot(arr, pivot_choice)
                start_time = time.time() 
                sorted_arr = quick_sort(arr, 0, n - 1, pivot)
                end_time = time.time() 
                f.write(f"{end_time - start_time:.10f}\n")
                
        with open("heap_sort/time_data_hs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = heap_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("merge_sort/time_data_ms_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = merge_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("insertion_sort/time_data_is_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = insertion_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("radix_sort/time_data_rs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
                temp1 = False
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = radix_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")

    temp1 = True
    for n in range(100,1001,100):
        arr = generate_reverse_sorted_list(n)
        with open("quick_sort/time_data_qs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")
                pivot = choose_pivot(arr, pivot_choice)
                start_time = time.time() 
                sorted_arr = quick_sort(arr, 0, n - 1, pivot)
                end_time = time.time() 
                f.write(f"{end_time - start_time:.10f}\n")
                
        with open("heap_sort/time_data_hs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = heap_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("merge_sort/time_data_ms_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = merge_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("insertion_sort/time_data_is_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = insertion_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("radix_sort/time_data_rs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
                temp1 = False
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = radix_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")

    temp1 = True
    for n in range(100,1001,100):
        arr = generate_random_list(n)
        with open("quick_sort/time_data_qs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")
                pivot = choose_pivot(arr, pivot_choice)
                start_time = time.time() 
                sorted_arr = quick_sort(arr, 0, n - 1, pivot)
                end_time = time.time() 
                f.write(f"{end_time - start_time:.10f}\n")
                
        with open("heap_sort/time_data_hs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = heap_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("merge_sort/time_data_ms_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = merge_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("insertion_sort/time_data_is_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = insertion_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("radix_sort/time_data_rs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
                temp1 = False
            f.write(f"{n}\t")
            start_time = time.time() 
            sorted_arr = radix_sort(arr)
            end_time = time.time() 
            f.write(f"{end_time - start_time:.10f}\n")

if __name__ == "__main__":
    main()


