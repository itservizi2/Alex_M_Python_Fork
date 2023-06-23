import string


def prima_functie():
    """
    Asta-i prima mea functie si ea afiseaza Hello From Function
    :return: None
    """
    print('Hello From Function')


# prima_functie(12) #eroare


def print_sum(a: int, b: int):
    """
    Aduna a si b
    :param a: primul numar
    :param b: al doilea numar
    :return: None
    """
    print(a + b)


print_sum(10, 24)


def clean_string(string_to_clean):
    """
    Cleans the string form punctation, whitspace and digits
    :param string_to_clean:
    :return:
    """
    for character in list(string.punctuation) + list(string.whitespace) + list(string.digits):
        string_to_clean = string_to_clean.replace(character, '')
    return string_to_clean


def longer_clean_string_bad(string1, string2):
    """
    Prints the string that contains most alphanumerical character (excluding whitespace and punctuation)
    :param string1:
    :param string2:
    :return: None
    """
    for character in list(string.punctuation) + list(string.whitespace) + list(string.digits):
        string1 = string1.replace(character, '')
    for character in list(string.punctuation) + list(string.whitespace) + list(string.digits):
        string2 = string1.replace(character, '')
    if len(string1) > len(string2):
        print(string1, 'is the longest')
    else:
        print(string2, 'is the longest')


def print_longer_clean_string(string1: str, string2: str):
    """
    Prints the string that contains most alphanumerical character (excluding whitespace and punctuation)
    :param string1:
    :param string2:
    :return: None
    """
    string1 = clean_string(string1)
    string2 = clean_string(string2)
    if len(string1) > len(string2):
        print(string1, 'is the longest')
    else:
        print(string2, 'is the longest')


print_longer_clean_string('12a', '123s')


def get_longer_clean_string(string1: str, string2: str):
    """
    Prints the string that contains most alphanumerical character (excluding whitespace and punctuation)
    :param string1:
    :param string2:
    :return: None
    """
    string1 = clean_string(string1)
    string2 = clean_string(string2)
    if len(string1) > len(string2):
        return string1
    return string2


result = get_longer_clean_string('12312asdjasd', 'lk;12;')
print(result)
