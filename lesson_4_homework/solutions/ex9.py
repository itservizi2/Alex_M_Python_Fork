"""
Scrieți un program_exemplu care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
password = input("Introduceți o parolă: ")

# if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password):
#     print("Parolă puternică.")
# else:
#     print("Parolă slabă.")

# # Corect si genial!
# if len(password) >= 8 and not password.isupper() and not password.islower():
#     print("Parolă puternică.")
# else:
#     print("Parola Slaba")
#
# With iteration
has_lower = has_upper = False

for char in password:
    if char.islower():
        has_lower = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_upper and has_upper:
    print("Puternica")
