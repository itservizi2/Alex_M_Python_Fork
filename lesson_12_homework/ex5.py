def is_valid_email(email):

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if "." not in domain:
        return False

    if len(domain.split(".")[-1]) < 2:
        return False
    return True


user_email = input("Enter an email address: ")
if is_valid_email(user_email):
    print("Valid email address")
else:
    print("Email address not valid")

