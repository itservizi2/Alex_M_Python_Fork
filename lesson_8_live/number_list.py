numbers = []
while True:
    value = input('Number or STOP')
    if value == 'STOP':
        break
    print(value)
    if value.isnumeric():
        print(value, "e int")
        continue
    if '.' not in value:
        print("nu poate fi numar")
        continue
    elemente = value.split('.', 1)
    stanga = elemente[0]
    dreapta = elemente[1]
    if stanga.isnumeric() and dreapta.isnumeric():
        print(f"{value} E float")
    else:
        print('Nu e float')
    # Solutia a doua
    clean_value = value.replace('.', '', 1)
    if clean_value.isnumeric():
        print(f"{float(value)} e float")
