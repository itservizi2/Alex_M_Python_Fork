"""
Avand lista de mai jos. Sortati list descrescatori si afisati rezultatul.
"""
list_2 = [5, 8, 2, 10, 4, 3, 1, 9]

# long way
list_2.sort()
print("Lista sortata crescator este:", list_2)
list_2.reverse()
print("Lista sortata descrescator este:", list_2)

# short way
list_2_2 = [5, 8, 2, 10, 4, 3, 1, 9]
list_2_2.sort(reverse=True)
print("Lista descrescatoare este:", list_2_2)

# Other ways

list_3 = [5, 8, 2, 10, 4, 3, 1, 9]

# Other way
sorted_list = sorted(list_3, reverse=True)
print(sorted_list)


# another other way
list_4 = [5, 8, 2, 10, 4, 3, 1, 9]
print(list(reversed(sorted(list_4))))
