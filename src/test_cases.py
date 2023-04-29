import random
import time
import sys
sys.path.append("..")
from quick_sort.quick_sort import quick_sort_version1
from quick_sort.quick_sort import quick_sort_version2
from quick_sort.quick_sort import quick_sort_version3
from heap_sort.heap_sort import heap_sort
from merge_sort.merge_sort import merge_sort
from radix_sort.radix_sort import radix_sort
from insertion_sort.insertion_sort import insertion_sort
sys.setrecursionlimit(10**6)

# Three types of functions to generate three different types of lists
def generate_random_list(n):
    list = [random.randint(1, 1001) for _ in range(n)]
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

def print_list(array3):
    print("The list is: [", end="")
    for i in range(len(array3)):
        if i < len(array3) - 1:
            print(array3[i], end=", ")
        else:
            print(array3[i], end="")
    print("]")

def main():
    # Boolean value
    temp1=True
    for n in range(1, 3000, 100):
        array1 = generate_sorted_list(n)
        temp = array1 # So that the array3ays are not dynamically changed at runtime
        
        with open("../heap_sort/csv files/time_data_hs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            heap_sort(temp)
            end_time = time.perf_counter() 
            temp = array1
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../merge_sort/csv files/time_data_ms_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            merge_sort(temp)
            end_time = time.perf_counter()
            temp = array1
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../insertion_sort/csv files/time_data_is_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            insertion_sort(temp)
            end_time = time.perf_counter() 
            temp = array1
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../radix_sort/csv files/time_data_rs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            radix_sort(temp)
            end_time = time.perf_counter() 
            f.write(f"{end_time - start_time:.10f}\n")

        with open("../quick_sort/csv files/time_data_qs_inc.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
                temp1 = False
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")

                if pivot_choice==1:
                    start_time = time.perf_counter() 
                    quick_sort_version1(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array1 
                    f.write(f"{end_time - start_time:.10f}\n")

                elif pivot_choice == 2:
                    start_time = time.perf_counter() 
                    quick_sort_version2(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array1 
                    f.write(f"{end_time - start_time:.10f}\n")

                else:
                    start_time = time.perf_counter() 
                    quick_sort_version3(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array1
                    f.write(f"{end_time - start_time:.10f}\n")

    temp1 = True
    for n in range(1, 3000, 100):
        array2 = generate_reverse_sorted_list(n)
        temp = array2

        with open("../heap_sort/csv files/time_data_hs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            heap_sort(temp)
            end_time = time.perf_counter() 
            temp = array2
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../merge_sort/csv files/time_data_ms_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            merge_sort(temp)
            end_time = time.perf_counter() 
            temp = array2
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../insertion_sort/csv files/time_data_is_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            insertion_sort(temp)
            end_time = time.perf_counter() 
            temp = array2
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../radix_sort/csv files/time_data_rs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            radix_sort(temp)
            end_time = time.perf_counter() 
            f.write(f"{end_time - start_time:.10f}\n")

        with open("../quick_sort/csv files/time_data_qs_dec.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
                temp1 = False
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")
                if pivot_choice==1:
                    start_time = time.perf_counter() 
                    quick_sort_version1(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array2 
                    f.write(f"{end_time - start_time:.10f}\n")

                elif pivot_choice==2:
                    start_time = time.perf_counter() 
                    quick_sort_version2(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array2
                    f.write(f"{end_time - start_time:.10f}\n")

                else:
                    start_time = time.perf_counter() 
                    quick_sort_version3(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array2 
                    f.write(f"{end_time - start_time:.10f}\n")
                

    temp1 = True
    for n in range(1, 3000, 100):
        array3 = generate_random_list(n)
        temp = array3
                
        with open("../heap_sort/csv files/time_data_hs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            heap_sort(temp)
            end_time = time.perf_counter() 
            temp = array3
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../merge_sort/csv files/time_data_ms_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            merge_sort(temp)
            end_time = time.perf_counter() 
            temp = array3
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../insertion_sort/csv files/time_data_is_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            insertion_sort(temp)
            end_time = time.perf_counter() 
            temp = array3
            f.write(f"{end_time - start_time:.10f}\n")
            
        with open("../radix_sort/csv files/time_data_rs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tTime taken (seconds)\n")
            f.write(f"{n}\t")
            start_time = time.perf_counter() 
            radix_sort(temp)
            end_time = time.perf_counter() 
            f.write(f"{end_time - start_time:.10f}\n")

        with open("../quick_sort/csv files/time_data_qs_ran.csv", "a") as f:
            if temp1:
                f.write("n\tPivot choice\tTime taken (seconds)\n")
                temp1 = False
            for pivot_choice in range(1, 4):
                f.write(f"{n}\t")
                f.write(f"{pivot_choice}\t")

                if pivot_choice==1:
                    start_time = time.perf_counter() 
                    quick_sort_version1(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array3 
                    f.write(f"{end_time - start_time:.10f}\n")

                elif pivot_choice==2:
                    start_time = time.perf_counter() 
                    quick_sort_version2(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array3 
                    f.write(f"{end_time - start_time:.10f}\n")

                else:
                    start_time = time.perf_counter() 
                    quick_sort_version3(temp, 0, n - 1)
                    end_time = time.perf_counter()
                    temp = array3 
                    f.write(f"{end_time - start_time:.10f}\n")

if __name__ == "__main__":
    main()
