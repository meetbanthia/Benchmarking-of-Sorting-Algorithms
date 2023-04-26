import csv
import matplotlib.pyplot as plt

input_size = []
times = []
with open('insertion_sort/time_data_is.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        input_size.append(int(row[0]))
        times.append(float(row[1]))

plt.plot(input_size, times)
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Insertion Sort Performance')
plt.show()

quick_sort = open("quick_sort/time_data_qs.csv", "wb")
radix_sort = open("radix_sort/time_data_rs.csv", "wb")
merge_sort = open("merge_sort/time_data_ms.csv", "wb")
insertion_sort = open("insertion_sort/time_data_is.csv", "wb")
heap_sort = open("heap_sort/time_data_hs.csv", "wb")

# Flush the files after extracting the relevant data
quick_sort.flush()
merge_sort.flush()
radix_sort.flush()
insertion_sort.flush()
heap_sort.flush()


