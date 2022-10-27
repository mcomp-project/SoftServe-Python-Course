# Calculate the sums of each row and each column of the matrix. Complete it with a column that contains the sums of
# the elements of the rows and a row whose elements are the sums of the elements of the columns.
import random

matrix = []
for i in range(3):  # For loop which implements matrix.
    matrix.append([])
    for j in range(3):
        matrix[i].append(random.randint(0, 101))
    print(matrix[i])

print('=' * 10)

matrix.append([])   # Need to add one more row.
for i in range(3):
    matrix[i].append(sum(matrix[i]))    # Sum function that count sum of every row.
    summary = 0
    for j in range(3):
        summary += matrix[j][i]    # "Count" way to count every column.
    matrix[-1].append(summary)     # Adds summary to matrices last element.

for i in matrix:    # Main loop which recreates matrix with Sum of row and columns.
    print(i)

print('=' * 10)
