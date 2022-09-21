import math

#variable with choice
choice = int(input(f'Please choose one of the geometrical figures:\n Rectangle(1)\n Triangle(2)\n Circle(3)\n[Only in numbers]->'))

#if statement for every option
if(choice == 1):
    rectangleside_a = float(input(f'Please input size of side A:\n'))
    rectangleside_b = float(input(f'Please input size of side B:\n'))
    print(f"The square of rectangle is {rectangleside_a * rectangleside_b}")

elif(choice == 2):
    triangleside_a = float(input(f"I need 3 sides of triangle. Please input the first one:\n"))
    triangleside_b = float(input(f"Please input the second one:\n"))
    triangleside_c = float(input(f"Please input the third one:\n"))
    p = ((triangleside_a + triangleside_b + triangleside_c)*0.5)
    print(f'The area of triangle is {math.sqrt(p*(p-triangleside_a)*(p-triangleside_b)*(p-triangleside_c))}')

elif(choice == 3):
    r = float(input(f"Please enter radius:"))
    print(f"Perimeter = {math.pi * 2 * r}; area = {math.pi * r **2}")


else:
    print(f'Wrong input.')
