"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.

Din sirul introdus creaza o lista de numere.

Afla suma elementelor pare si a celor impare din lista si afiseaz-o.
"""

numbers = input("Introduceti un sir de numere, separate prin virgula de la consola: ")
number_list = [int(num) for num in numbers.split(",")]

even_sum = sum(num for num in number_list if num % 2 == 0)
odd_sum = sum(num for num in number_list if num % 2 != 0)

print("Suma numerelor pare:", even_sum)
print("Suma numerelor impare:", odd_sum)

