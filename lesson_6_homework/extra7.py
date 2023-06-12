## Exercițiul 7:

# Scrieți un program care primește un număr întreg pozitiv ca intrare și afișează suma tuturor numerelor de la 1 până la acel număr.

number = int(input("Introduceți un număr întreg pozitiv: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print("Suma tuturor numerelor de la 1 la", number, "este:", sum)

