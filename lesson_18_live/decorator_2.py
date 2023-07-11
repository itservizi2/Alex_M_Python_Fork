def ensure_string(function):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            new_args.append(str(arg))
        for k, v in kwargs.items():
            kwargs[k] = str(v)
        function(*new_args, **kwargs)

    return wrapper


@ensure_string
def example_String_function(a: str, b, c, d):
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(a, b, c, d)


example_String_function(1, [12], bool, d=None)
