"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
password = str(input("introduceti parola "))
conditia_lungime_minima = len(password) >= 8
conditia_prezenta_majuscule = any(char.isupper() for char in password)
conditia_prezenta_minuscule = any(char.islower() for char in password)

if conditia_lungime_minima and conditia_prezenta_majuscule and conditia_prezenta_minuscule:
    print("parola puternica")
else:
    print("parola slaba")

