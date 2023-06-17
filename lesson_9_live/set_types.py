my_set = {1, 1.0, 1, False, None, ('o', 'k')}
print(my_set)

my_tuple = ('o', 'k')
same_tuple = ('o', 'k')

print(my_tuple == same_tuple)

# Adding a mutable
my_set.add(my_tuple)
