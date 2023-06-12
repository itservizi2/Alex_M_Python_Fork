# Improve the password generator
"""
Inbunatatiti acest generator de parole, astfel incat sa fie posibil sa genereze parole ce contin atat litere,
cat si cifre si caractere speciale.
"""

import string
import random

all_letters = list(string.ascii_letters)
all_numbers = list(map(str, range(10)))
# all_numbers = list(string.digits)
all_punctuation = list(string.punctuation)
list_for_password = all_letters + all_numbers + all_punctuation
pass_length = int(input('Pass length: '))

password = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(list_for_password))
    password += list_for_password[letter_index]
print(f"The password: {password}")
