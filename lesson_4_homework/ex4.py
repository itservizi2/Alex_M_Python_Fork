"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

str1 = input("insert the string : ")
is_a = bool(str1[1] == "a")
if is_a:
    print(f"Expresia litera 'a' se află pe a 2-a poziţie este {is_a}")
else:
    print(f"Expresia litera 'a' se află pe a 2-a poziţie este {is_a}")

