# Write a program that calculates the sum of all even numbers between a and b (inclusive). The values ​​of a and b
# are entered by the user.


# Initialize values A, B and counter "total".
valueA = float(input(f'Enter number A:\n'))
valueB = float(input(f'Enter number B:\n'))
total = 0 
counter = 0 + valueA 
	
while counter <= valueB:
	if counter % 2 == 0:
		print('{0}'.format(counter))
		total = total + counter
	counter += 1
		
print(f'The Sum of even numbers from {valueA} to {valueB} is {total}')
