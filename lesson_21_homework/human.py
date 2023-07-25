from datetime import date


class Human:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        return f"{self.get_full_name()}, age {self.get_age()}"


from datetime import date
from human import Human

human = Human("Vasile", "Petrescu", date(1978, 3, 14))
print(human)
