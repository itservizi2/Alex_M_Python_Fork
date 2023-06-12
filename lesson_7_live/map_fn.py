map(str, range(10))

char_list = ['1', '2', '3']
print(char_list)
result = list(map(int, char_list))
result = list(map(list, char_list))
result = list(map(tuple, char_list))
result = list(map(float, char_list))
print(result)
