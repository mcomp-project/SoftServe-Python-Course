# A real number is given. Determine what this number is: positive, negative, zero.
num = float(input(f"Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
