"""
Scrieți un program care solicită utilizatorului să introducă un șir de caractere și numără numărul de caractere din șir
(excluzând spațiile).
"""

sir = input("Tastati sirul: ")

counter = 0
for element in sir:
    if not element == " ":
        counter += 1
print(counter, "excluzand spatiile.")
