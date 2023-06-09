"""Exercise 3: Ticket Pricing
Write a program that calculates the ticket price based on the age of the person. The price is determined as follows:
- Children (age 0-5): Free
- Students (age 6-18): $5
- Adults (age 19 and above): $10"""

age = int(input('Age:'))

if age < 6:
    print('Free')
elif 6 <= age <= 18:
    print('$5')
else:
    print('10$')
