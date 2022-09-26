# User enters ten natural numbers greater than 2. Count how many of them are numbers that are multiples of 5.

count = 0 # Implement the variable for number of multiples of 5.
for count in range(0,10): # Loop in range from 0 to 10.(must be 10 loops)
	number = int(input(f'Enter 10 natural numbers bigger than 2:\n'))# Input variable.
	if (number > 2): # If statement to test if number is greater than 2.
		if(number % 5 == 0): # If statement to count multiples of 5.
			print(f'Number of multiples of 5 is {count}')
			count = count + 1 # Adds every time when number is a multiple of 5.
	else:
		print('Error, entered number is smaller than 2.')
