import csv
import matplotlib.pyplot as plt

pivot_choices = []
times = []
with open('time_data.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        pivot_choices.append(int(row[0]))
        times.append(float(row[1]))

plt.bar(pivot_choices, times)
plt.xlabel('Pivot Choice')
plt.ylabel('Time (seconds)')
plt.title('Quick Sort Performance')
plt.show()
