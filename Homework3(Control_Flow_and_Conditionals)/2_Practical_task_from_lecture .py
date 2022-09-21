number = int(input('Enter natural number\n'))
if number > 0:
	if (number % 2) == 0: print('The number is even') 
	else: print ('The provided number is odd') 
	if (number % 4) == 0: print(f'{number} is multiple of 4')
	else: print(f'{number} is not multiple of 4')
else: print('It`s not a natural number')
	

