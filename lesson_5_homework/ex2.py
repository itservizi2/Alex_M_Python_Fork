"""
Avand lista de mai jos. Sortati list descrescatori si afisati rezultatul.
"""

#metoda1 aceeasi lista
list_2 = [5, 8, 2, 10, 4, 3, 1, 9]
list_2.sort(reverse=True)
print(list_2)

#metoda2 crearea altei liste
list_2a = [5, 8, 2, 10, 4, 3, 1, 9]
list_2a_sortata = sorted(list_2a, reverse=True)
print(list_2a_sortata)

