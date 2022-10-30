# User enters number; determine the percentage of positive and negative numbers. When input 0 - finish.

total = 0
positive = 0

while True:
    
    number = int(input(f'Enter the number. If you want to finish enter "0": \n'))

    if number > 0:
        positive += 1
    elif number == 0:
        print('finish')
        break
    total += 1
    
    print(f'The percentage of positive numbers:', positive/total * 100, '%','The percentage of negative numbers: ', 100-(positive/total *100), '%')
