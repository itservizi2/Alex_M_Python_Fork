"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""
# Solution
sir = input("Introdu sirul:")
# Calcularea numarului total de caractere
print("Lungimea sirului", len(sir))
# Calcularea numarului total de vocale in sir

sir_upper = sir.upper()

count_vocale = (sir_upper.count('A')) + (sir_upper.count('E')) + \
               (sir_upper.count('I')) + (sir_upper.count('O')) + \
               (sir_upper.count('U')) + (sir_upper.count('Ă')) + \
               (sir_upper.count('Ȃ')) + (sir_upper.count('Î'))

sir_fara_punct = sir.replace(' ', '').replace('.', '').replace('!', '').replace(',', '').replace('?', '')

count_consane = len(sir_fara_punct) - count_vocale

print('Consoane', count_consane)
print('Vocale', count_vocale)
print('Total', len(sir_fara_punct))

# # Calcularea numarului total de consoane in sir
# print((sir.lower().count('b')) + (sir.lower().count('c')) +
#       (sir.lower().count('d')) + (sir.lower().count('f')) +
#       (sir.lower().count('h')) + (sir.lower().count('j')) +
#       (sir.lower().count('k')) + (sir.lower().count('l')) +
#       (sir.lower().count('m')) + (sir.lower().count('n')) +
#       (sir.lower().count('p')) + (sir.lower().count('q')) +
#       (sir.lower().count('r')) + (sir.lower().count('s')) +
#       (sir.lower().count('ş')) + (sir.lower().count('t')) +
#       (sir.lower().count('ț')) + (sir.lower().count('v')) +
#       (sir.lower().count('w')) + (sir.lower().count('x')) +
#       (sir.lower().count('z')) + (sir.lower().count('y')))
