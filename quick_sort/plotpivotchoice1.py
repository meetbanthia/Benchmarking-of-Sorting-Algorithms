import csv
import matplotlib.pyplot as plt

input_size = []
times_sorted = []
times_rev_sorted = []
times_random = []

with open('csv files/time_data_qs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "1":
            times_sorted.append(float(row[2]))

with open('csv files/time_data_qs_ran.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "1":
            input_size.append(row[0])
            times_random.append(float(row[2]))

with open('csv files/time_data_qs_dec.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "1":
            times_rev_sorted.append(float(row[2]))

plt.plot(input_size, times_sorted,label = "Sorted")
plt.plot(input_size, times_rev_sorted, label = "Reverse Sorted")
plt.plot(input_size, times_random, label = "Random")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Pivot Choice 1')

plt.legend()
plt.show()





