from lesson_22_live.inheritance_example.Animal import Animal
from lesson_22_live.inheritance_example.Dog import Dog


class SmallDog(Dog):

    def eat(self):
        super().eat()

    def bark(self):
        return f"{super().bark()} in a cute voice"


if __name__ == '__main__':
    dog = SmallDog("Kuzea", "Chihuahua")
    other_animal = Animal("Tuzik", "Dog")
    print(dog.bark())
    dog.eat()
    dog.sleep()
