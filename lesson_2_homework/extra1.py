## Exercițiul 1: Atribuirea variabilelor
# Scrie un program care atribuie valori celor două variabile, `a` și `b`, și apoi schimbă valorile lor. Afișează valorile lui `a` și `b` înainte și după schimbare.


#metoda 1
a = input("insert a: ")
b = input("insert b: ")
temp = a
print("valoarea a inainte de schimbare este ", a)
print("valoarea b inainte de schimbare este ", b)
a = b
b = temp
print("valoarea a dupa schimbare este ", a)
print("valoarea b dupa schimbare este ", temp)


#metoda 2
print()
a = input("insert a: ")
b = input("insert b: ")
print("valoarea a inainte de schimbare este ", a)
print("valoarea b inainte de schimbare este ", b)
a, b = b, a
print("valoarea a dupa schimbare este ", a)
print("valoarea b dupa schimbare este ", b)
