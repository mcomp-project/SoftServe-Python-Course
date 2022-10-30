# Given the number P and the number H.
# The user enters a sequence of numbers.
# Determine: the sum of those numbers that are less than P; product of numbers greater than H;
# the number of numbers in the range of values ​​from P to H.
# When entering a number equal to P or H, stop the calculation and display the result


p = 10
h = 20

sum_P = 0
prod_H = 1
range_p_h = 0
number = 0

while number != p and number != h:
    number = int(input('Enter number:\n'))
    if number < p:
        sum_P += number
    elif p <= number <= h:
        range_p_h += 1
    else:
        prod_H *= number

print('The sum of numbers < P:', sum_P)
print('Product of numbers greater H:', prod_H)
print('Number of numbers in the range of values from P to H:', range_p_h)
