class Animal:

    def __init__(self, name, animal_type="Dog"):
        self.name = name
        self.age = "1 day"
        self.animal_type = animal_type


my_kuzea = Animal("Kuzea")
my_tuzea = Animal("Tuzea")
print(my_kuzea.name)
print(my_kuzea.age)
print(my_kuzea.animal_type)

my_kuzea.animal_type = 'Cat'
print(my_kuzea.animal_type)
print(my_tuzea.animal_type)
