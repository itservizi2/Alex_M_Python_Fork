from collections import defaultdict

from lesson_14_live.print_utils import print_dict


def get_default_inventory():
    return ['apple', 'stick', 'pen']


inventar_jucatori = defaultdict(get_default_inventory)

print_dict(inventar_jucatori)

# Marius eats an apple
inventar_jucatori['Marius'].remove('apple')

print_dict(inventar_jucatori)
