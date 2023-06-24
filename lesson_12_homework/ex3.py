def check_password_strength(password):

    if len(password) < 8:
        return False

    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    if not has_uppercase:
        return False

    has_lowercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
            break
    if not has_lowercase:
        return False

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False

    has_special = False
    for char in password:
        if char in "!@#$%^&*":
            has_special = True
            break
    if not has_special:
        return False
    return True


password = input("Enter a password: ")
strength = check_password_strength(password)
if strength:
    print("Password strength: True (meets the criteria)")
else:
    print("Password strength: False (does not meet the criteria)")
