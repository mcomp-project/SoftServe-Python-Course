import random 	# Import random tool to use it for random.randint .


count = 0 # Counting every try.
random.randint(0,101) # Random integer from 0 to 100.
print(f'You have to guess the number from 0 to 100. My advice is to use binary algoritm..\n')

while count < 10: #Used while loop.
    b = int(input(f'You have {10 - count} attempts. Make your choice:\n'))
    count += 1 # Counts every try, you will see if statement next.
	if count >= 10:
        print(f'Sorry, number was {a}')
        break
    elif b == a:
        print(f'YES! You did it in', count, 'try!')
        break
    elif b > a:
        print(f'Number is smaller!')
    elif b < a:
        print(f'Number is bigger!')

