# Is it possible to place a round stage with radius R in a square hall of square S so that there is a passage was at
# least K from the wall to the stage?

import math

# let`s make 3 variables to count the formula
l_hall = int(input(f'Please, input the length of the hall wall\n'))
radius = float(input(f'Please, input the radius of the stage\n'))
distance = int(input(f'Please enter passage distance\n'))

# using {math.pi} from module math
stage_area = math.pi*radius**2
hall_s = l_hall **2

# if statement to answer the question
if (hall_s - distance) > stage_area:
    print(f'The hall area will be large enough to accommodate the stage inside, when stage area is {stage_area} m`2 and the hall area is {hall_s} m`2.\n')
else:
    print(f'The area of the stage, which is {stage_area}, will not fit hall with area of {hall_s} m`2.\n')