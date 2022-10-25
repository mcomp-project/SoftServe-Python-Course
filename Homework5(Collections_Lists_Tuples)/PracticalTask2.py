#   Form a matrix of numbers from 0 to 999, display it on the screen. Count the number of two-digit numbers in it.
import numpy as np  # We need numpy to implement an array.

a = np.array([np.arange(0, 1000)])  # Vector from 0 till 999.
count = 0
for row in a:   # For loop that 'touches' every element of the array.
    for col in row:
        if len(str(col)) == 2:  # Len function helps to find how many digits in element.
            count += 1
print(a)
print('Number of two-digit numbers is:', count)
