## Exercițiul 1:

# Scrieți un program care solicită utilizatorului să introducă un șir de caractere și numără numărul de caractere din
# șir (excluzând spațiile).

user_input = input("Introduceti un sir de caractere: ")
character_count = len(user_input.replace(" ", ""))
print("Numarul de caractere din sir (excluzand spatii):", character_count)
