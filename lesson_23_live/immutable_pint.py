class ImPoint:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self._locked = True

    def __setattr__(self, key, value):
        if hasattr(self, '_locked') and self._locked:
            raise Exception()
        super().__setattr__(key, value)

    def __str__(self):
        return f"{self.x}, {self.y}"


a = ImPoint(1, 2)
print(a)


class SomeObject():

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __setattr__(self, key, value):
        if key not in ['a', 'b']:
            raise Exception('Not allowed to change atts')
        super().__setattr__(key, value)

    def __getattr__(self, item):
        print('Get-attr is called')
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return None


a = SomeObject('a', 'b')
print(a.a)
print(a.b)
# a.c = 10
print(a.c)

a.a = 10
