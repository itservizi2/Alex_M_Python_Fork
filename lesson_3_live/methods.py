my_stirng = "HEllo world"
print(my_stirng.count('H'))
print(my_stirng.count('h'))

my_stirng = "Hello hello hello"
print(my_stirng.count("Hello"))
print(my_stirng.count("hello"))

my_stirng = "Hello HeLLo helLO"
lower_string = my_stirng.lower()
print(my_stirng)
print(lower_string)
print(lower_string.count("hello"))

new_str = my_stirng.replace('l', 'L', 2)

print(new_str)
