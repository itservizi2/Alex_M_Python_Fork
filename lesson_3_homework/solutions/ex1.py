"""1.
Creați 2 variabile x şi y, a căror valoare este citită de la tastatură.

Folosiți funcţia int() pentru a transforma valorile citite în numere întregi.

* Definiţi după aceasta variabila suma care va fi egală cu suma lui x şi y.
* Definiţi variabila **diff** care va fi egală cu x - y (diferenţa lui x şi y).
* Definiţi variabila **rest_impart** care va fi egală cu restul împărţirii lui x la y.
* Definiţi variabila **mult** care va fi egală cu x înmulţit cu y.
* Definiţi variabila **power3** care va fi egală cu x la puterea 3.

Afișați toate rezultatele
"""

# Solution
x = int(input('x:'))
y = int(input('y:'))
suma = x + y
differenta = x - y
rest_impart = x % y
inmultirea = x * y
power_3 = x ** 3
print("Suma", suma)
print("Diff", differenta)
print("Rest impart", rest_impart)
print("Inmult", inmultirea)
print("Cube", power_3)
