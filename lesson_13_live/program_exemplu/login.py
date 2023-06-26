from utils.validators import is_valid_email, is_valid_password


def login_user():
    email_pt_inregistate = input('email:')
    password = input('password:')

    if is_valid_email(email_pt_inregistate) and is_valid_password(password):
        print("Registration can be done")
    else:
        print('Invalid data')
