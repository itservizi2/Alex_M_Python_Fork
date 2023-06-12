# Solution
print("Welcome to our time convertor!")
time_format = int(input("Pentru a converti formatul de 24 ore tastati '24' pentru 12 ore tastati '12'\n "))
if time_format == 24:
    time = input("Format: hh:mm PM sau hh:mm AM.\n")
    time_hour = int(time[0:2])
    time_minutes1 = str(time[3:4])
    time_minutes2 = str(time[4:5])
    time_minutes = time_minutes1 + time_minutes2
    time_minutes_int = int(time_minutes)
    time_meridian = time[6:8]
    time_meridian_upper = time_meridian.upper()
    if time_meridian_upper == "PM":
        if time_minutes_int > 0:
            time_hour += 12
            print(f"Ora in formatul de 24 ore este:\n{time_hour}:{time_minutes}")
        else:
            print(f"Ora in formatul de 24 ore este:\n{time_hour}:{time_minutes}")
    else:
        print(f"Ora in formatul de 24 ore este:\n{time_hour}:{time_minutes}")
elif time_format == 12:
    time = input("Format: hh:mm sau hh:mm.\n")
    time_hour = int(time[0:2])
    time_minutes1 = str(time[3:4])
    time_minutes2 = str(time[4:5])
    time_minutes = time_minutes1 + time_minutes2
    time_minutes_int = int(time_minutes)
    time_meridian = time[6:8]
    time_meridian_upper = time_meridian.upper()
    if time_hour == 24:
        time_hour = 12
        print(f"Ora in formatul de 12 ore este:\n {time_hour}:{time_minutes} AM")
    elif time_hour > 12 and time_minutes_int >= 0:
        time_hour -= 12
        print(f"Ora in formatul de 12 ore este:\n {time_hour}:{time_minutes} PM")
    elif time_hour == 12 and time_minutes_int >= 0:
        print(f"Ora in formatul de 12 ore este:\n {time_hour}:{time_minutes} PM")
    else:
        print(f"Ora in formatul de 12 ore este:\n {time_hour}:{time_minutes} AM")
