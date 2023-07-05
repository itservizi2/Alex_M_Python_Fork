import json

with open('numbers.json', 'r') as file:
    str_data = file.read()
    print(type(str_data))
    print(str_data[1])
    file.seek(0)
    data_from_file = json.load(file)
    print(type(data_from_file))
    print(data_from_file[1])
