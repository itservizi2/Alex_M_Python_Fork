from lesson_23_live.decorators import DateUtils


class Plane:

    def __init__(self, initial_height=100):
        self.height = initial_height

        self.upper_limit = 10000
        self.lower_bound = 0

    def fly_up(self, height=100):
        if self.height + height > self.upper_limit:
            raise Exception(f'Can\'t go higher than {self.upper_limit}')
        else:
            self.height += height

    def fly_down(self, height=100):
        if self.height - height <= self.lower_bound:
            raise Exception(f'Can\'t go lower than {self.lower_bound}')
        else:
            self.height -= height

    def __str__(self):
        return f"Plane at height: {self.height}"


if __name__ == '__main__':
    plane = Plane()
    while True:
        inpt = input('u for up and d for down')
        if inpt == 'u':
            plane.fly_up()
        elif inpt == 'd':
            try:
                plane.fly_down()
            except Exception as ex:
                print(ex)
                print(f"plane is now at {plane.height}")
                val = int(input('Hight to fly down'))
                plane.fly_down(val)
        print(plane)
