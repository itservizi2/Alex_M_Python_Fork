"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.

Din sirul introdus creaza o lista de numere.

Afla suma elementelor pare si a celor impare din lista si afiseazo.
"""

numbers = input("Introduceti un sir de numere separate prin virgula: ")
str_list_of_numbers = numbers.split(',')
list_of_numbers = map(int, str_list_of_numbers)

sum_pare = 0
sum_impare = 0
for x in list_of_numbers:
    if x % 2 == 0:
        sum_pare += x
    else:
        sum_impare += x

print(f"Suma numerelor pare: {sum_pare}.\nSuma numerelor impare: {sum_impare}.")
