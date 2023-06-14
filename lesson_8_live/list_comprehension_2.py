numere_prin_virgula = input('Numere separate prin virgula')

suma = 0

for number in numere_prin_virgula.split(','):
    number = int(number)
    suma += number

print(suma)

print(
    sum(
        [
            int(el) for
            el in
            numere_prin_virgula.split(',')
        ]
    )
)
