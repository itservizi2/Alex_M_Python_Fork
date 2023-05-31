username = input('Username')
days_since_last_login = int(input('Last Login'))

print(f"Hello, {username}, it's been {days_since_last_login} since you were last logged in.")

welcome_email_title = f"Welcome {username}"
welcome_email_body = f"Hello, {username}, thanks for registering on our platform"
print(welcome_email_title)
print(welcome_email_body)
