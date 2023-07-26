class Produs:

    def __init__(self, nume, pret):
        self.name = nume
        self._price = pret

    def get_price_for_qty(self, qty):
        return qty * self._price

    def get_reducere_from_child(self, qty):
        self.get_reducerea(qty)
