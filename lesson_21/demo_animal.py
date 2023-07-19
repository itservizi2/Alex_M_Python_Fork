class Animal:

    def __init__(self, nume, animal_type='Animal necunoscut', numar_labe=0, numar_aripi=0, sunet=''):
        self._animal_type = animal_type
        self._numar_labe = numar_labe
        self._numar_aripi = numar_aripi
        self._nume = nume
        self._sunet = sunet

    def reprezinta(self):
        print(
            f'Un animal de tip {self._animal_type} cu {self._numar_labe} labe si {self._numar_aripi} aripi cu numele {self._nume}.')

    def fa_sunet(self):
        print(self._sunet)

    def schimba_nume(self, nume_nou):
        if type(nume_nou) != str:
            raise Exception('Name must be string')
        self._nume = nume_nou

    def clone(self, nume):
        return Animal(
            self._animal_type,
            self._numar_labe,
            self._numar_aripi,
            nume,
            sunet=self._sunet
        )


gasca = Animal("Cornel", "Gasca", 2, 2, "Gaa")
gasca.reprezinta()
gasca.schimba_nume(12)
gasca.reprezinta()
gasca._nume = 12
print(gasca._nume)
gasca.reprezinta()

gasca.reprezinta()
gasca.fa_sunet()

caine = Animal("Kuzea", animal_type="Caine", numar_labe=4, sunet="Woof")
caine.reprezinta()
caine.fa_sunet()

alt_animal = Animal("Bob")
alt_animal.reprezinta()
alt_animal.fa_sunet()
