import csv
import matplotlib.pyplot as plt

input_size = []
times_sorted = []
times_rev_sorted = []
times_random = []

qs_csv_files = ['time_data_qs_inc.csv', 'time_data_qs_ran.csv', 'time_data_qs_dec.csv']

for file in qs_csv_files:
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
        next(reader) # skip the header row
        for row in reader:
            if len(input_size) == 0:
                input_size.append(row[0])
            if row[1]=='3':
                times_sorted.append(float(row[2]))

plt.plot(input_size, times_sorted,label = "Sorted")
plt.plot(input_size, times_rev_sorted, label = "Reverse Sorted")
plt.plot(input_size, times_random, label = "Random")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Pivot Choice 3')

plt.legend()
plt.show()






