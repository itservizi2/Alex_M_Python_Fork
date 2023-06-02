# Creaza un program care va cere de la utilizator:
#
# Adresa de email
# Numele de utilizator
# Și va afisa aceasta infromatie in urmatorul format:
#
# Emailul pentru Marius a fost expediat cu succes pe adresa de email mariustricolici@hotmail.com
#
# Pentru adresa de email: mariustricolici@hotmail.com Si numele de utilizator: Marius

email = input("Adresa de email")
username = input("Numele de utilizator")

mesaj = "Email pentru ", username, "a fost expediat cu succes pe adresa de email", email
mesaj = f"Email pentru {username} a fost expediat cu succes pe adresa de email {email}"

print(mesaj)
