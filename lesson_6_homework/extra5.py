## Exercițiul 5:

# Scrieți un program care primește două șiruri de caractere ca intrare și verifică dacă acestea sunt anagrame (adică un
# cuvânt poate fi format prin rearanjarea literelor altui cuvânt).


s1 = input("Introduceți primul șir: ")
s2 = input("Introduceți al doilea șir: ")

s1 = s1.lower()
s2 = s2.lower()

sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)

if sorted_s1 == sorted_s2:
    print("Sirurile sunt anagrame ")
else:
    print("Sirurile nu sunt anagrame ")
