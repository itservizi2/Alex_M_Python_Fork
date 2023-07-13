'''
Creati un program python cu ajutorul careia vor fi gasite toate elementele dintr-o lista de string-uri care sunt palindroame.
Avand lista ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] rezultatul va fi ['php', 'aaa'].

Note: Puteti folosi functia filter pentru a filtra elementele unei colectii.
'''

all_list_elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']


def is_palindrom(value):
    return value == value[::-1]


b = list(filter(is_palindrom, all_list_elements))
print(b)

b = list(filter(lambda el: el == el[::-1], all_list_elements))
print(b)
