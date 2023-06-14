nr = 1251251242353452341

prime = True

for a in range(2, nr // 2 + 1):
    print("checking", a)
    if nr % a == 0:
        prime = False
        break

print(prime)

"""
Scrieți un program care utilizează o buclă while pentru a verifica dacă un număr
întreg pozitiv dat n este un număr prim.
 Un număr prim este un număr întreg pozitiv mai mare decât 1 care nu are divizori pozitivi în afară de 1 și el
însuși. Programul ar trebui să afișeze dacă numărul este prim sau nu.
"""

integer = int(input("Introduceti un numar pozitiv:\n"))
if integer > 1:
    divisor = 2
    while divisor * divisor <= integer:
        print("Checking", divisor)
        if integer % divisor == 0:
            print(f'{integer} nu este prim')
            break
        divisor += 1
    else:
        print(f'Este prim')
else:
    print(f'{integer} Nu este prim')
