from lesson_22_live.inheritance_example.Animal import Animal


class Bird(Animal):

    def fly(self):
        print(f'{self.name} is flying')
