"""
Avand lista de mai jos.

Adaugati in ea elementele **4**, **5** si **6**.

Afișați rezultatele
"""

list_1 = [1, 2, 3]
print(f"Lista initiala este: {list_1}")

list_1.append(4)
print(f"Lista noua, cu adaugarea unui element(4) la lista intiala cu ajutorul .append va arata astfel: {list_1} ")

list_2 = [5, 6]
list_1 += list_2
# echivalent cu
# list_1.extend(list_2)
print(f"Lista noua, cu concatenarea cu alta lista(5,6) la lista intiala va arata astfel: {list_1} ")

# Tot merge
# list_1 = [1, 2, 3]
# list_1[len(list_1):] = {4, 5, 6}
# print(list_1)
