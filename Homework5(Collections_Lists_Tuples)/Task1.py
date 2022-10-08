# Fill in one list with random numbers, another with numbers entered from the keyboard,
# and write the sums of the corresponding elements of the first two lists in the third one.
# Display the contents of the lists on the screen.
import random

random_list = [random.randint(0, 10) for x in range(0, 5)]  # List of 5 random numbers will be implemented.
user_list = []  # Implement a list where will be user's input of numbers.

for number in range(0, 5):  # For loop to input numbers to user's list.
    number = (int(input('Please, enter 5 numbers from 0 to 10:\n')))
    user_list.append(number)

# List comprehension that counts sums of the corresponding elements of the lists.
sum_list = [user_list[x] + random_list[x] for x in range(len(random_list))]
print('List of random numbers:\n', random_list, '\n'
      'List of numbers that entered user:\n', user_list, '\n'
      'List of the sums of the corresponding elements of the first two lists:\n', sum_list)
