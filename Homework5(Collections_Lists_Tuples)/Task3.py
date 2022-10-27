# Find the maximum elements of minimum elements of the matrix column.
import random


matrix = []
minimums = []
print('Usual matrix:')
for i in range(3):  # Matrix, made by for loop.
    matrix.append([])
    for j in range(3):
        matrix[i].append(random.randint(0, 11))

for i in range(len(matrix)):
    minimum = int(matrix[i][0])
    for j in range(len(matrix)):
        if minimum > matrix[j][i]:
            minimum = matrix[j][i]
    minimums.append(minimum)

for i in matrix:
    print(i)
print("Range of minimal numbers in matrix is:\n", minimums)
print("Biggest element among smallest is:", (max(minimums)))
