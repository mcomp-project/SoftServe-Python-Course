fuelCapacity = int(input('Please enter the fuel capacity in percents(100max)\n'))
if fuelCapacity >= 10:
	print(f'The sensor light is green')
else:
	print(f'The sensor light is red')
