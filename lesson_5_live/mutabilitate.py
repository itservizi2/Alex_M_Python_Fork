# Mutabilitate


# Exemplu imutabil

str1 = 'Marius'
# Str2 e copie
str2 = str1
# Modificarea la str1 nu modifica str2
str1 += '!'
print(str1, str2)

nr1 = 1
nr2 = nr1
nr1 += 1
print(nr1, nr2)

# Exemplu mutabil (liste)

list1 = ['Hello']
# list2 are o referinta la list1
list2 = list1
list1.append('World')
print(list1, list2)

# pentru a crea o copie, cream o lista noua

list1 = ['Hello']
list2 = list(list1)
list1.append('World')
print(list1, list2)

nested_list = [[1, 2, 3], [1, 2, 3]]
nested_list_copy = nested_list
nested_list[0].append(1)
nested_list.append(1)
print(nested_list, nested_list_copy)
