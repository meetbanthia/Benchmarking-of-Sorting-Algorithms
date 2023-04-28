# Benchmarking-of-Sorting-Algorithms
This is an assignment in Design and Analysis of Algorithms(CS253) course. The objective of the assignment is to compare the performance of various traditional sorting 
algorithms taught during the semester and plot graphs for them which showcase their preformance for various cases.<br />
The instructions to run the code the code is as follows.
* Fork of the repository.
* Clone the repository using the HTTPS key.
## Running the Code
After cloning the repository navigate to the root directory of the project.<br />
* Each of the 5 sorting algorithms are present in their respective folders. 
* Since there is data present in the csv files hence execute ```src/python flush.py``` before running the code. 
* The csv files present for each sorting algorithm contains the input size and the time taken for sorting for all the three types of arrays i.e. increasing array, randomly generated array and decreasing array.
* Execute ```src/python test_cases.py``` for generating the csv files.
* Navigate to the ```quick_sort``` folder and run each of the ```plotpivotchoice``` files to generate the graphs which compare the performance of quick sort in the 3 different choice of pivots.
* Navigate to the ```Q4``` and execute the files in the folder to see the performance of each algorithm vs the other in different cases.
> **_NOTE:_**  After completing the visualisation make sure to run ```flush.py``` otherwise the programs run into errors.
