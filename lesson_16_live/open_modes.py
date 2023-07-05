with open('example.txt', 'r') as file:
    # print(file.read())
    while True:
        data = file.readline()
        if not data:
            break
        print(data)

with open('example.txt', 'a') as file:
    file.writelines(["Hello", "Something"])
