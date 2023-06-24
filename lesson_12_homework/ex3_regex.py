import re

def check_password_strength(password):

    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True
password = input("Enter a password: ")
strength = check_password_strength(password)
if strength:
    print("Password strength: True (satisface conditiile)")
else:
    print("Password strength: False (nu satisface conditiile)")
