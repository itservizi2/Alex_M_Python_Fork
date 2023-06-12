## Exercițiul 10:

# Scrieți un program care solicită utilizatorului să introducă un număr întreg pozitiv și afișează un model de triunghi
# utilizând asteriscuri. De exemplu, dacă utilizatorul introduce 5, programul ar trebui să afișeze:

num = int(input("Introduceti un integer pozitiv: "))

for i in range(1, num + 1):
    print("*" * i)

