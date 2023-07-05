with open('example', 'w') as file:
    file.write('Hello\n')
    file.write('Hello\n')
    file.write('Hello\n')
    file.write('Hello\n')

file2 = open('example2.txt', 'w')
file2.write('Hello3')
file2.write('Hello2')
file2.write('Hello1')
file2.write('Hello0')
file2.close()
