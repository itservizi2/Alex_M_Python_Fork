from lesson_22_live.inheritance_example.Animal import Animal
from lesson_22_live.inheritance_example.Bird import Bird
from lesson_22_live.inheritance_example.Dog import Dog
from lesson_22_live.inheritance_example.SmallDog import SmallDog

dog = Dog("Tuzik", "Cihuahua")
small_dog = SmallDog("Kuzea", "Taxa")
bird = Bird("Kesha", "Bird")

print(isinstance(dog, Animal))
print(isinstance(bird, Animal))
print(isinstance(small_dog, Dog))
print(isinstance(small_dog, Animal))
print(isinstance(dog, SmallDog))

print(issubclass(type(dog), SmallDog))
print(issubclass(SmallDog, type(dog)))
