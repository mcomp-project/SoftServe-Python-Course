# Enter a number, letter or special character from the keyboard and return the entry index to the corresponding tuple accordingly.

atuple = (1, 2, 3, 4, 5, "A", "B", "C", "D", "E", "A1", "A2", "A3", "A4", "A5", "\u0394", "\U0001F600")
print(atuple)

a = input("Enter something from that list, please:\n")
if a.isnumeric():
    print(atuple.index(int(a)))
else:
    print(atuple.index(a))