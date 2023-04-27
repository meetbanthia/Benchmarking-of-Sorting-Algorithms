import csv
import matplotlib.pyplot as plt

input_size = []

times_qs = []
times_ms = []
times_hs = []
times_rs = []
times_is = []

avg_csv_files = ['insertion_sort/time_data_is_ran.csv', 'merge_sort/time_data_ms_ran.csv', 
                 'heap_sort/time_data_hs_ran.csv', 'radix_sort/time_data_rs_ran.csv']
# plot for average case comparision of all the 5 sorts
for file in avg_csv_files: 
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
        next(reader) # skip the header row
        if len(input_size) == 0:
            input_size.append(row[0])
        for row in reader:
            input_size.append(row[0])
            times_is.append(float(row[1]))

with open('quick_sort/time_data_qs_ran.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1]=='2':
            times_qs.append(float(row[2]))

plt.plot(input_size, times_is,label = "Insertion Sort")
plt.plot(input_size, times_ms, label = "Merge Sort")
plt.plot(input_size, times_rs, label = "Radix Sort")
plt.plot(input_size, times_qs, label = "Quick Sort")
plt.plot(input_size, times_hs, label = "Heap Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithms Average Case Performance')

plt.legend()
plt.show()






