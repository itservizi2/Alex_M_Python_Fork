"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare, atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""

nume = str(input("introduceti numele "))
nume_transformat = nume[0].capitalize() + nume[1:]
is_capital = bool(nume[0].isupper())
if is_capital:
    print(f"numele ce incepe cu majuscula este {nume} ")
else:
    print(f"numele ce incepe cu majuscula este {nume_transformat} ")

