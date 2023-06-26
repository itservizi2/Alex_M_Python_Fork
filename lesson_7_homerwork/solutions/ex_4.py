"""
Scrieți un program_exemplu care utilizează o buclă while pentru a verifica dacă un număr
întreg pozitiv dat n este un număr prim.
 Un număr prim este un număr întreg pozitiv mai mare decât 1 care nu are divizori pozitivi în afară de 1 și el
însuși. Programul ar trebui să afișeze dacă numărul este prim sau nu.
"""

integer = int(input("Introduceti un numar pozitiv:\n"))
este_prim = False
if integer > 1:
    este_prim = True
    divisor = 2
    while divisor * divisor <= integer and este_prim:
        print("Checking", divisor)
        if integer % divisor == 0:
            este_prim = False
        divisor += 1
if este_prim:
    print(f"{integer} este un numar prim.")
else:
    print(f"{integer} nu este un numar prim.")
