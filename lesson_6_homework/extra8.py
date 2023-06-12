## Exercițiul 8:

# Scrieți un program care solicită utilizatorului să introducă un șir de caractere și verifică dacă acesta este un
# palindrom (adică se citește la fel de la stânga la dreapta și de la dreapta la stânga).

string = input("Introduceti un sir : ")
string = string.lower().replace(" ", "")

if string == string[::-1]:
    print("Sirul este palindrom.")
else:
    print("Sirul nu este palindrom.")

