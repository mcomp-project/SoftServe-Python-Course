# #The user enters a number, the program must display its description. For example, "positive one-digit",
# "negative two-digit", etc.

number = int(input(f'Enter the number:\n'))
digit = len(str(number))  # len() - returns numbers of "symbols" in variable(100 = 3 digits)

if number < 0:
    digit -= 1

if number < 0:
    print(f'{number} is {digit}-digit negative number.\n')
elif number > 0:
    print(f'{number} is {digit}-digit positive number.\n')
else:
    print(f'Zero is a neutral number.')
