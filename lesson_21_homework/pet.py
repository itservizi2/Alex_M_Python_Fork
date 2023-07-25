from datetime import date


class Pet:
    def __init__(self, name, pet_type, favorite_food):
        self.name = name
        self.type = pet_type
        self.favorite_food = favorite_food

    def __str__(self):
        return f"{self.type} called {self.name} that loves {self.favorite_food}"


class HumanWithPet:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.pets = []

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

    def adopt_pet(self, pet):
        self.pets.append(pet)

    def giveaway_pet(self, pet):
        self.pets.remove(pet)

    def __str__(self):
        pet_desc = ""
        if len(self.pets) == 1:
            pet_desc = f"with a pet: {self.pets[0]}"
        elif len(self.pets) > 1:
            pet_desc = f"with {len(self.pets)} pets: "
            for pet in self.pets:
                pet_desc += str(pet) + ", "
        return f"{self.get_full_name()}, age {self.get_age()} {pet_desc.rstrip(', ')}"


cat = Pet("Garfield", "Cat", "lasagna")
dog = Pet("Kuzea", "Dog", "bones")

human = HumanWithPet("Anton", "Petrosian", date(1989, 3, 31))
print(human)

human.adopt_pet(cat)
print(human)

human.adopt_pet(dog)
print(human)

human.giveaway_pet(dog)
print(human)
