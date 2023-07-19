class Animal:

    def __init__(self, name, animal_type="Dog"):
        self.name = name
        self.age = "1 day"
        self.animal_type = animal_type

    def say_hi(self):
        print(f'{self.animal_type} {self.name} says hi')


my_kuzea = Animal("Kuzea")
my_barsic = Animal("Barsic")

my_kuzea.say_hi()
my_kuzea.animal_type = 'Cat'
my_kuzea.say_hi()

my_barsic.say_hi()
