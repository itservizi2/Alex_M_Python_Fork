"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""

propozitie = input("Introduceți propoziția: ")
subsir_tinta = input("Introduceți subșirul țintă: ")
subsir_inlocuire = input("Introduceți subșirul de înlocuire: ")

propozitie_noua = propozitie.replace(subsir_tinta, subsir_inlocuire)

print(f"Propoziția modificata este {propozitie_noua}")

