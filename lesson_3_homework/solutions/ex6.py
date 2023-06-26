"""
 Extrageți un subșir de caractere
Scrieți un program_exemplu care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""
# Solution

sir = input('Sirul')
start = int(input(f"Index de inceput, de la 1 pan la {len(sir)}"))
finish = int(input(f"Index de sfarsit, de la {start} pan la {len(sir)}"))
subsir = sir[start - 1:finish]
print(subsir)
