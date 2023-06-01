# Creaza un program care va cere de la utilizator:
#
# Adresa de email
# Numele de utilizator
# Și va afisa aceasta infromatie in urmatorul format:
#
# Emailul pentru Marius a fost expediat cu succes pe adresa de email mariustricolici@hotmail.com
#
# Pentru adresa de email: mariustricolici@hotmail.com Si numele de utilizator: Marius

email = input("Introduceti email: ")
nume = input("Introduceti nume : ")
print('Emailul pentru ' + nume + ' a fost expediat cu succes pe adresa ' + email)
print('Emailul pentru {} a fost expediat cu succes pe adresa {} '.format(nume, email))


