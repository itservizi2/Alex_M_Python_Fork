nr_list = [1, 2, 3]

suma = 0

for element in nr_list:
    suma += element

print("Media", suma / len(nr_list))

nr_list = [1, 2, 3, 5, 6, 10]

suma = 0
nr_pare = 0

for element in nr_list:
    if element % 2 == 0:
        suma += element
        nr_pare += 1

print("Media", suma / nr_pare)
