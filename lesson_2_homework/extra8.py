## Exercițiul 8: Convertor de timp
#Scrie un program care preia numărul de secunde ca intrare și îl convertește în ore, minute și secunde. Afișează timpul convertit.

secunde_in_total = int(input("introdu nr secunde : "))
ore = secunde_in_total // 3600
minute = (secunde_in_total % 3600) // 60
secunde = (secunde_in_total % 3600) % 60
print("Timpul convertit este: {} ore, {} minute și {} secunde".format(ore, minute, secunde))
