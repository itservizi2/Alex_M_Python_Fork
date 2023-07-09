import time
from datetime import datetime


# validam data introdusa
def validate_date(input_date):
    try:
        d = datetime.strptime(input_date, '%d/%m/%Y %H:%M')
        now = datetime.now()
        if d < now:
            print("The entered date is from the past, please enter a valid future date")
            return False
        elif (d - now).days > 365:
            print('The entered date should not be more than a year in the future')
            return False
        else:
            return True
    except ValueError:
        return False


# obtinem data
valid_date = False
while not valid_date:
    input_date = input("Enter a date and time as dd/mm/YYYY HH:MM: ")
    valid_date = validate_date(input_date)

# obtinem numele la eveniment
event = input("Enter event name: ")

# convertim data introdusa din format string in datetime object
target_date = datetime.strptime(input_date, '%d/%m/%Y %H:%M')

# loop pina cind ajungem la data deziderata
while datetime.now() < target_date:
    time_left = target_date - datetime.now()
    # calculam timp ramas
    days, seconds = time_left.days, time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    # afisam timp ramas
    print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds left until {event}")
    # update la fiecare secunda
    time.sleep(1)

print(f"{event} is here!")
