def multiplcator(*args):
    mult = 1
    for el in args:
        mult *= el
    return mult


def suprafata_dreptunghi(a, b):
    return multiplcator(a, b)


def nr_la_cub(a):
    return multiplcator(a, a, a)
