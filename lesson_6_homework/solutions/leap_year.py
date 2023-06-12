year = int(input("Please enter the year:\n"))
if year % 4 != 0:
    print(f"The year {year} is Not a leap year.")
elif year % 100 == 0 and year % 400 != 0:
    print(f"The year {year} is Not a leap year.")
else:
    print(f"The year {year} is a leap year.")
# Solution2
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
# Solution 3
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")
