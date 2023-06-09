"""
Exercise 2: Leap Year Checker
Write a program that takes a year as input and determines whether it is a
 leap year or not.
  A leap year is divisible by 4,
   but not divisible by 100 unless it is also
    divisible by 400.
"""

year = int(input('Year:'))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))