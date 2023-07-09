import calendar
import json
from datetime import datetime, timedelta

DATE_TIME_FORMAT = "%d/%m/%Y %H:%M"


def get_data_from_file() -> list[dict]:
    try:
        with open('user_data.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_to_file(data: list[dict]):
    with open('user_data.json', 'w') as file:
        return json.dump(data, file)


def add_user():
    username = input('UserName')
    all_users = get_data_from_file()
    if username in [user['username'] for user in all_users]:
        raise Exception('User alread exists')
    registration_date = datetime.now()
    all_users.append(
        dict(
            username=username,
            registration_date=registration_date.strftime(DATE_TIME_FORMAT)
        )
    )
    save_data_to_file(data=all_users)


while True:
    all_users = get_data_from_file()
    print("Current user are")
    for user in all_users:
        reg_date_str = user["registration_date"]
        reg_date_obj = datetime.strptime(reg_date_str, DATE_TIME_FORMAT)
        is_leap = calendar.isleap(datetime.now().year + 1)
        ainversary = reg_date_obj + timedelta(days=366 if is_leap else 365)
        print(
            f'{user["username"]} regisred on {user["registration_date"]} that has aniversary on {ainversary}'
        )
    print()
    try:
        add_user()
    except Exception as ex:
        print(f"Error: {ex}")
