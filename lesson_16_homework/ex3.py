filename = input("Enter a filename: ")
with open(filename, "w") as file:
    text = input("Type some text: ")
    file.write(text)
with open(filename, "r") as file:
    text = file.read()
    print("Text from file:", text)
