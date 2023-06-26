def split_csv(csv, sep=','):
    return csv.split(sep)


def make_string_from_list(list_to_str, combinator='; '):
    if not list_to_str:
        return "Empty List"
    if combinator == '':
        raise ValueError('Not allowed to use empty cominator')
    return combinator.join(list_to_str)


if __name__ == '__main__':
    try:
        print(make_string_from_list(['12', '3'], ''))
    except ValueError:
        print("Something went wrong")
