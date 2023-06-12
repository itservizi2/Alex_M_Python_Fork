## Exercițiul 4:

# Scrieți un program care solicită utilizatorului să introducă un număr și afișează toate numerele pare de la 1 la acel număr.

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, end=" ")

