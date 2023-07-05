with open('example.txt') as file:
    data = file.read(5)
    print(data)
    other_data = file.read()
    print(other_data)
    other_other_data = file.read()
    print(other_other_data)
    file.seek(10, 0)
    other_other_data = file.read()
    print(other_other_data)

with open('example.txt', 'r+') as file:
    file.seek(1)
    file.write('INTRUDER')
