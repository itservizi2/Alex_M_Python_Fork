from datetime import datetime, timedelta


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point at {self.x} {self.y}"

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"{other} is not a point")
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"{other} is not a point")
        if self.x > other.x:
            return True
        if self.x == other.x:
            if self.y > other.y:
                return True
            else:
                return False
        return False

    def __lt__(self, other):
        return not self > other

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __repr__(self):
        return f"Point at x:{self.x} y:{self.y}"

    def __mod__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __len__(self):
        return 0


p1 = Point(1, 2)

p1 += 2

p2 = Point(1, 2)
p3 = Point(2, 1)

print(p1 == p2)
print(p1 != p3)
print(p1 != p2)

if Point(-1, 0):
    print('Yey')

print(p1)

date_time = datetime.now()
time_delta = timedelta(days=1)

date_time + time_delta

time_delta + date_time

len(p1)
