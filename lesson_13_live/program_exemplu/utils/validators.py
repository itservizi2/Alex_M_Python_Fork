import re


def is_valid_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*]", password):
        return False

    return True


def is_valid_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if "." not in domain:
        return False

    last_dot_index = domain.rindex(".")
    domain_name = domain[last_dot_index + 1:]

    if len(domain_name) < 2:
        return False

    return True


def is_valid_username():
    pass


def is_valid_birthday_date():
    pass


if __name__ == '__main__':
    email = input("Enter an email address: ")
    valid_email = is_valid_email(email)
    print(f"Valid email address: {valid_email}")
    password = input("Enter a password: ")
    password_strength = is_valid_password(password)
    strength_message = "meets the criteria" if password_strength else "does not meet the criteria"
    print(f"Password strength: {password_strength} ({strength_message})")


def is_valid_birthday_date():
    pass
