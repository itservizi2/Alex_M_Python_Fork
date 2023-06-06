"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
str1 = str(input("introduceti fraza : "))
last_symbol = str1[-1]
if last_symbol == "?":
    print("Aceasta este o întrebare ")
else:
    print("Aceasta nu este o întrebare ")
