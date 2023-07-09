import datetime

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
dob_str = input("Enter your date of birth (in the format DD/MM/YYYY): ")

dob = datetime.datetime.strptime(dob_str, '%d/%m/%Y').date()
now = datetime.date.today()

delta1 = datetime.date(now.year, dob.month, dob.day)
delta2 = datetime.date(now.year + 1, dob.month, dob.day)
delta = delta1 if delta1 > now else delta2
days_until_birthday = (delta - now).days

print(f"{first_name} {last_name} has birthday in {days_until_birthday} days")
