"""
Time converter V2

Write a program that takes time from user input in the following format:
 "11:20 PM" or "02:00 AM".
And converts it to 24-Hour format.
"23:20" or "02:00"

Combine the solution, with the solution from the live lesson,
and make it possible that the user can decide which conversion to do.
From 24 hour to 12 hour, or vice-versa.


Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
"""

# Cerem timp de introducere de la utilizator
input_time = input("Introduceti timpul in format '11:20 PM' sau '02:00 AM' (specificarea AM sau PM este obligatorie): ")

# Împărțim input în componente
time_components = input_time.split()
time_digits = time_components[0].split(":")

# Convertim în format de 24 de ore
if time_components[1].upper() == "PM":
    new_hour = str(int(time_digits[0]) + 12)
    if new_hour == "24":
        new_hour = "12"
    new_time = "{}:{}".format(new_hour, time_digits[1])
else:
    if time_digits[0] == "12":
        new_hour = "00"
    else:
        new_hour = time_digits[0]
    new_time = "{}:{}".format(new_hour, time_digits[1])

# Convertim în format de 12 ore dacă dorim
convert_to_12_hour = input("Convertim in 12-hour format? (Y/N) ")
if convert_to_12_hour.upper() == "Y":
    hour_digits = new_time.split(":")[0]
    minutes = new_time.split(":")[1]
    if int(hour_digits) >= 12:
        am_pm = "PM"
        if hour_digits != "12":
            hour_digits = str(int(hour_digits) - 12)
    else:
        am_pm = "AM"
        if hour_digits == "00":
            hour_digits = "12"
    new_time = "{}:{} {}".format(hour_digits, minutes, am_pm)

# Print the new time
print("Ora convertita:", new_time)




