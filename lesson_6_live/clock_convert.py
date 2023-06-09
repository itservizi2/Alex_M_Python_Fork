"""
Write a program that takes a time in 24-hour format as input (e.g., 13:45)
and converts it to 12-hour format (e.g., 1:45 PM).

"""
time = input('Time in format HH:MM')
hours_and_minutes_list = time.split(':')
hours, minutes = hours_and_minutes_list[0], hours_and_minutes_list[1]

pm = 'AM'

if hours >= '12':
    if hours != '12':
        hours = str(int(hours) - 12)
    pm = 'PM'

print(f"{hours}:{minutes} {pm}")

# Harder acasa
time = input('time in format HH:MM AM/PM')
