a = int(input("Value for a\n"))
b = int(input("Value for b\n"))

print(f'Value a = {a}, value b = {b}')
a = a+b
b = a-b
a = a-b
print(f'We just swap it: a = {a}, b = {b}')