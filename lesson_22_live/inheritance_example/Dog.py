from lesson_22_live.inheritance_example.Animal import Animal


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def eat(self):
        print(f"{self.breed} {self.name} is eating")

    def bark(self):
        return f"{self.breed} {self.name} is barking"

    def child_bark(self):
        from lesson_22_live.inheritance_example.SmallDog import SmallDog
        SmallDog.bark(self)


if __name__ == '__main__':
    dog = Dog("Kuzea", "Chihuahua")
    other_animal = Animal("Tuzik", "Dog")
    print(dog.bark())
    dog.eat()
    dog.sleep()
