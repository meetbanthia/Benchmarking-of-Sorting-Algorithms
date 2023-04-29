import csv
import matplotlib.pyplot as plt

input_size = []

times_qs = []
times_ms = []
times_hs = []
times_rs = []
times_is = []

# Plot for best case comparision of all the 5 sorts
with open('../insertion_sort/csv files/time_data_is_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        input_size.append(row[0])
        times_is.append(float(row[1]))

with open('../merge_sort/csv files/time_data_ms_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        times_ms.append(float(row[1]))

with open('../heap_sort/csv files/time_data_hs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        times_hs.append(float(row[1]))

with open('../radix_sort/csv files/time_data_rs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        times_rs.append(float(row[1]))

with open('../quick_sort/csv files/time_data_qs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        if row[1]=='3':
            times_qs.append(float(row[2]))

plt.plot(input_size, times_is, label = "Insertion Sort")
plt.plot(input_size, times_ms, label = "Merge Sort")
plt.plot(input_size, times_rs, label = "Radix Sort")
plt.plot(input_size, times_qs, label = "Quick Sort")
plt.plot(input_size, times_hs, label = "Heap Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithms Best Case Performance')

plt.legend()
plt.show()
