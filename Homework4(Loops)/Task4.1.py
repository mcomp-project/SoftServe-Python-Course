# Python Program to Draw a Rectangle using For loop.

r, c, i, j = 0, 0, None, None
# r - denotes the number of rows.
# c - denotes the number of columns.

print ("-----Enter the number of rows & columns-----")
r = int (input ())
c = int (input ())

print ("\n-----The rectangle pattern is-----\n")
for i in range (1, r + 1):
	for j in range (1, c + 1):
		if i == 1 or i == r or j == 1 or j == c:
			print (end="*  ")
		else:
			print(end="   ")

	print (end="\n\n")
