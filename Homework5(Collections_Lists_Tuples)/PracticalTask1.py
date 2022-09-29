#Find the elements that occur only once in the list, and display them on the screen. That is, find and display unique elements of the array.

for element in range(0,5): # Implement a loop with the list inside.
	element = [int(input(f'Enter the number to the list:\n'))] # Main list.
	unique_num = [] # List where will be unique numbers.
	for x in element: # Looking for unique numbers in 'element'.
		num = x
		if element.count(num) < 2: # If statement with "count" method to find the unique one.
			unique_num.append(num)
print("The unique number in list is",unique_num)
