"""1.	Creați 2 variabile x şi y, a căror valoare este citită de la tastatură.

Folosiți funcţia int() pentru a transforma valorile citite în numere întregi.

* Definiţi după aceasta variabila suma care va fi egală cu suma lui x şi y.
* Definiţi variabila **diff** care va fi egală cu x - y (diferenţa lui x şi y).
* Definiţi variabila **rest_impart** care va fi egală cu restul împărţirii lui x la y.
* Definiţi variabila **mult** care va fi egală cu x înmulţit cu y.
* Definiţi variabila **power3** care va fi egală cu x la puterea 3.

Afișați toate rezultatele

"""
x = int(float(input("insert x: ")))
y = int(float(input("insert y: ")))

suma = x + y
print(f"suma = {suma}")

diff = x - y
print(f"diff = {diff}")

rest_impart = x % y
print(f"rest_impart = {rest_impart}")

mult = x * y
print(f"mult = {mult}")

power = x ** 3
print(f"power = {power}")

