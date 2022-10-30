# The YEAR is known. Determine whether this year is intercalary and to what century this year belongs.
year = int(input(f'Please enter the year:\n'))
century = (year//100+1)

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'Year {year} is intercalary\n')

elif year < 1582:
    print(f'Year must be later than 1582.\n')

elif year == 1582:
    print(f'Year {year} is intercalary\n')

else:
    print(f'Year {year} is non-leap year.\n')

print(f'It`s {century}`th century.\n')
