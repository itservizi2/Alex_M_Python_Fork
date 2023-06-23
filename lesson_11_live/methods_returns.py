# Functions that return nothing

var1 = 'Hello'
result_of_print = print(var1)
print(result_of_print)

# Functie ce intoarce rezultat

result_of_input = input('Type somethign')
print(result_of_input)

# Metoda poate modifica variabila mutabila, fara a intoarce un rezultat

my_list = []
result_of_append = my_list.append('Hello')
print(my_list)
print(result_of_append)

# Metode care intorc variabila modificata

str1 = 'Hey?!'
result_of_replace = str1.replace('?', '')
print(result_of_replace)
print(str1)
str1 = result_of_replace
print(str1)

# Metode care modifica si retuneaza

new_list = ['1', '2']
result_of_pop = new_list.pop(1)
print(result_of_pop)
print(new_list)
