#Write a program that calculates the sum of all odd numbers between a and b (inclusive). The values ​​of a and b are entered by the user.


# Initialize values A, B and counter "total".
valueA = int(input(f'Enter number A:\n'))
valueB = int(input(f'Enter number B:\n'))
total = 0 
counter = 0 + valueA 

for counter in range(valueA, valueB+1):
	if (counter % 2 != 0):
		print(counter)
		total += counter
		

print(f'The Sum of odd numbers from {valueA} to {valueB} is {total}')
