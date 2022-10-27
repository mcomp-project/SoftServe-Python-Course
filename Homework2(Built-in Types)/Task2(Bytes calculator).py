# Implement a calculator that translates the amount of information entered by the user in bytes into kilobytes and
# megabytes.
number = int(input(f"please enter the number of bytes\n"))
kilo = number / 1024
mb = kilo / 1024

print(f'The number of bytes are {number}, it`s {kilo} kilobytes and {mb} megabytes')
