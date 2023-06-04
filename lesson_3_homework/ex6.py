"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""
sir = input("introduceti sirul de caractere : ")
lungime_sir = len(sir)
max_positive_index = lungime_sir - 1
start_index = 0
index1 = int(input(f"introduceti index1 folosind valori din intervalul {start_index} si {max_positive_index} "))
index2 = int(input(f"introduceti index2 folosind valori din intervalul {index1} si {max_positive_index} "))
user_defined_subsir = sir[index1:index2]
print(f"user defined substring is {user_defined_subsir} ")

