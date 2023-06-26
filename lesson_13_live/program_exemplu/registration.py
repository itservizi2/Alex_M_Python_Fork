from utils.validators import is_valid_email, is_valid_password, is_valid_birthday_date
from login import login_user


def register_user():
    email_pt_inregistate = input('email:')
    password = input('password:')

    if is_valid_email(email_pt_inregistate) and is_valid_password(password):
        print("Registration can be done")
    else:
        print('Invalid data')

    birth = input('Birth')
    is_valid_birthday_date(birth)
