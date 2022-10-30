# The amount of money is known. Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible.
money = int(input(f'Please enter the amount of money:'))

if money % 200 == 0:
    mg = money//200
    print(f"{money} can be exchanged by 200UAH for {mg} times.")
elif money % 100 == 0:
    mg = money//100
    print(f'{money} can be exchanged by 100UAH for {mg} times.')
elif money % 10 == 0:
    print(f'{money} can be exchanged by 10UAH for {mg} times.')
else:
    mg = money // 200, '200UAH', (money % 200) // 100, '100UAH', ((money % 200) % 100) // 10, '10UAH', ((money % 200) % 100) % 10, '1UAH'
    print(f'{money} can be exchanged for banknotes such as {mg}')    
