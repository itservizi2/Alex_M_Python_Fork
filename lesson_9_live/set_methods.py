nr_list = [a for a in input("Numere separate prin spatiu").split()]
print(nr_list)

nr_set = set(nr_list)
for number in nr_list:
    print(f'Numer {number} is used', nr_list.count(number))

# ^ # Symetric difference
