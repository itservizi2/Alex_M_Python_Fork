my_list = list()
print(my_list)
my_list = [1, 2, 3]
print(my_list)

print(my_list[0])
print(my_list[-1])

my_list = ['Marius', 'Ion', 'Mircea']
print(my_list[0])
print(my_list[0][0])

string = 'Marius e programator'
marius_list = list(string)
print(marius_list)
print(len(marius_list) == len(string))
print(marius_list == string)
print(marius_list[0])

new_marius_string = ",".join(marius_list)
print(new_marius_string)

nested_list = [[1, 2],
               [2, 3]]
nested_list = [['one', 2, 3],
               [2, 3, 4],
               [5, 7, 10]]
print(nested_list[2][1])
print(nested_list[2][2])

list_exmaple = list('1')

# tuples

tup = 1, 2, 3
print(tup)

list_from_tup = list(tup)
print(list_from_tup)
