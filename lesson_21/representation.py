class Animal:

    def __init__(self, nume, animal_type='Animal necunoscut', numar_labe=0, numar_aripi=0, sunet=''):
        self._animal_type = animal_type
        self._numar_labe = numar_labe
        self._numar_aripi = numar_aripi
        self._nume = nume
        self._sunet = sunet

    def __str__(self):
        return f'Un animal de tip {self._animal_type} cu {self._numar_labe} labe si {self._numar_aripi} aripi cu numele {self._nume}.'

    def reprezinta(self):
        print(self)


gasca = Animal("Cornel", "Gasca", 2, 2, "Gaa")
print(gasca)
gasca.reprezinta()
