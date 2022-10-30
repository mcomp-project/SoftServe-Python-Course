# Create a dictionary in which the keys are numbers and the values are their string interpretation. Write a program
# that converts this dictionary, in which the keys will be strings and the values - numbers.
oldDict = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
}
print(oldDict)  # Printing original dictionary.
print('-'*30)
newDict = dict([(value, key) for key, value in oldDict.items()])    # Dict with list comprehension to swap the values.
for i in newDict:
    print(i, ":", newDict[i])   # Printing new dict after swapping keys and values.
