from datetime import datetime


def client_registration():
    name, surname = input("Introdu numele si prenumele: ").split()
    date_string = input("Enter a date (DD/MM/YYYY): ")
    date = datetime.strptime(date_string, "%d/%m/%Y")
    current_date = datetime.now()

    # Calculez ziua de nastere
    next_birthday = datetime(current_date.year, date.month, date.day)

    # Dacă ziua de naștere următoare a avut deja loc în acest an, calculez pentru anul viitor.
    if next_birthday < current_date:
        next_birthday = datetime(current_date.year + 1, date.month, date.day)

    # Calculez numărul de zile până la următoarea zi de naștere.
    days_until_birthday = (next_birthday - current_date).days
    print(f"Clientul {name}, {surname} va avea ziua de nastere in {days_until_birthday} zile")


if __name__ == '__main__':
    client_registration()
