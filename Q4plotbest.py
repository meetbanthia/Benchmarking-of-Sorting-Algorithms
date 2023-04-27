import csv
import matplotlib.pyplot as plt

input_size = []

times_qs = []
times_ms = []
times_hs = []
times_rs = []
times_is = []

inc_csv_files = ['insertion_sort/time_data_is_inc.csv', 'merge_sort/time_data_ms_inc.csv', 
                 'heap_sort/time_data_hs_inc.csv', 'radix_sort/time_data_rs_inc.csv']

# Plot for average case comparision of all the 5 sorts
for file in inc_csv_files: 
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
        next(reader) # skip the header row
        if len(input_size) == 0:
            input_size.append(row[0])
        for row in reader:
            input_size.append(row[0])
            times_is.append(float(row[1]))

with open('quick_sort/time_data_qs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        if row[1]=='3':
            times_qs.append(float(row[2]))

plt.plot(input_size, times_is, marker = 'o', label = "Insertion Sort")
plt.plot(input_size, times_ms, marker = 'o', label = "Merge Sort")
plt.plot(input_size, times_rs, marker = 'o', label = "Radix Sort")
plt.plot(input_size, times_qs, marker = 'o', label = "Quick Sort")
plt.plot(input_size, times_hs, marker = 'o', label = "Heap Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithms Best Case Performance')

plt.legend()
plt.show()
