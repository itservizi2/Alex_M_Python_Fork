class NumbersList(list):
    def __init__(self, *args):
        for arg in args:
            self.append(arg)

    def append(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only integers and floats can be added to NumbersList")
        super().append(value)

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        return sum(self) / len(self)


nums = NumbersList(1, 2, 3, 4, 5)
print(nums)

nums.append(6)
print(nums)
# nums.append("7") # afiseaza TypeError si comentez ca sa nu cada la rulare

print("Sum = ", nums.get_sum())
print("Average = ", nums.get_average())
