# Template, potential din extern
template = """
Hello, {username}

I want to notify you that your payment of {amount} is due on {date}.
If you are having trouble with the payment, please contact us at {contact_email}

Best regards,
Software Company
"""

username = input("un")
amount = input("am")
date = input("date")
contact_email = input("ce")

message = template.format(
    username=username,
    amount=amount,
    date=date,
    contact_email=contact_email
)

print(
    message
)
