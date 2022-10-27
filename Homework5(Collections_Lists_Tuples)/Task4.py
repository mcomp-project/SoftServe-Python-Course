# Divide the tuple into several ones, each of which contains only numbers, only letters, etc.

atuple = (1, 2, 3, 4, 5, "A", "B", "C", "D", "E", "A1", "A2", "A3", "A4", "A5", "\u0394", "\U0001F600")
numbers_tuple = tuple([x for x in atuple if isinstance(x, int)])
letters_tiple = tuple([x for x in atuple if str(x).isalpha()])
other_tuple = tuple([x for x in atuple if not str(x).isalpha() and not isinstance(x, int)])

print(numbers_tuple)
print(letters_tiple)
print(other_tuple)
