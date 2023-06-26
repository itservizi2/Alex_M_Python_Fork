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


email = input("Enter an email address: ")

valid_email = is_valid_email(email)
print(f"Valid email address: {valid_email}")