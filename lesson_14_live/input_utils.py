

def input_list_of_numbers_safe():
    """
    Will generate a list of numbers from input while handling any potential error
    :return:
    """
    list_of_numbers = []
    while True:
        value = input('Introdu un numar sau apasa enter pentru a opri')
        if value == '':
            break
        try:
            list_of_numbers.append(int(value))
        except ValueError:
            print('Nu ai introdus un numar, te rog mai incearca')
    return list_of_numbers



