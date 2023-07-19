import time


class Comanda:

    def __init__(self, numar_comanda, client):
        self.numar = numar_comanda
        self.client = client
        self.status = 'Initial'

    def afiseaza_comanda(self):
        print(f"Comanda {self.numar} pentru {self.client} are statutul {self.status}")

    def proceseaza_comanda(self):
        print('Procesez comanda')
        self.status = 'In Procesare'

    def finalizeaza_comanda(self):
        print('Finalizez comanda')
        self.status = 'Procesat'


comanda_mea = Comanda('1', 'Mine')
comanda_mea.afiseaza_comanda()
comanda_mea.proceseaza_comanda()
comanda_mea.afiseaza_comanda()
time.sleep(1)
comanda_mea.finalizeaza_comanda()
comanda_mea.afiseaza_comanda()
