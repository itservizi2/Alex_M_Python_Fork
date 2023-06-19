example_dict = {'name': 'Marius', 'age': 25, 'hobbies': ['Programming']}

# Shallow copy
copy_of_dict = example_dict.copy()

print(copy_of_dict, example_dict)

# Copy is shallow, so it will change
example_dict['hobbies'].append('Fishing')

print(copy_of_dict, example_dict)

copy_of_dict['name'] = 'Andrei'

print(copy_of_dict, example_dict)

# Extracting only keys or only values
print(copy_of_dict.values())
print(copy_of_dict.keys())

# Taking something out
del copy_of_dict['age']
print(copy_of_dict)

# using pop
hobbies = copy_of_dict.pop('hobbies')
print(hobbies)
print(copy_of_dict)
