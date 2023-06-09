# Exercitiu cu numerele

x_str = input('Introdu nr de numere')
if not x_str.isnumeric():
    print("Nu ain introdus un numar")
    exit()
x = int(x_str)
suma = 0
if x > 0:
    for time in range(x):
        suma += int(input(f'Numarul {time + 1}:'))
    print(f'Media este: {suma / x}')
else:
    print('Nu pot afla media la 0 numere')
print(f'Media este: {suma / x}')