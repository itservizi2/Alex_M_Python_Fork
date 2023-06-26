import re


def check_password_strength(password):
    matches = 0

    if len(password) >= 8:
        matches += 1

    if re.search(r"[A-Z]", password):
        matches += 1

    if re.search(r"[a-z]", password):
        matches += 1

    if re.search(r"\d", password):
        matches += 1

    if re.search(r"[!@#$%^&*]", password):
        matches += 1

    # 0 - forate slaba
    # 1 -2 slaba
    # 3-4 medium
    # 5 puternica
    if matches == 1:
        print('Parola e foarte slaba')
    elif matches == 2:
        print('Parola e slaba')
    elif matches in [3, 4]:
        print('Parola e medium')
    else:
        print('Parola e puternica')


password = input("Enter a password: ")

password_strength = check_password_strength(password)
# strength_message = "meets the criteria" if password_strength else "does not meet the criteria"
# print(f"Password strength: {password_strength} ({strength_message})")
