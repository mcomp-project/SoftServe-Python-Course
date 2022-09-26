from turtle import *
# Display a rectangle. 1`st character - fill, 2nd - outline.

a = input(f'Please enter the color of "fill":')
b = input(f'Please enter the color of outline:')
color(b, a)

begin_fill()
for i in range(2):
    forward(150)
    right(90)
    forward(75)
    right(90)
end_fill() 
hideturtle()    
