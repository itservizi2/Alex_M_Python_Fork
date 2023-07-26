from datetime import datetime, date


class Customer:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 date_of_birth: datetime,
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        birth_date = self.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return max(age, 0)

    def __str__(self):
        return f"{self.full_name()} varsta {self.get_age()}"


if __name__ == '__main__':
    c = Customer('Marius', "Tricolici", datetime(2022, 9, 30))
    assert c.get_age() == 0
    c = Customer('Marius', "Tricolici", datetime(1998, 1, 30))
    assert c.get_age() == 25
    c = Customer('Marius', "Tricolici", datetime(2023, 9, 30))
    assert c.get_age() == 0, f"Age is {c.get_age()} and not 0"
    print(c)
