from lesson_22_live.exmaple_store.Produs import Produs


class ProdusLaReducere(Produs):

    def __init__(self, nume, pret, reducere):
        super().__init__(nume, pret)
        # Reducerea este nr procente: ex 20 = 20%
        self.reducere = reducere

    def get_price_for_qty(self, qty):
        return super().get_price_for_qty(qty) - self.get_reducerea(qty)

    def get_reducerea(self, qty):
        return super().get_price_for_qty(qty) * self.reducere / 100


if __name__ == '__main__':
    p1 = Produs("Bere", 24)
    p1.get_reducere_from_child(3)

if __name__ == '__main__':
    p1 = Produs('Bere', 24)
    p2 = Produs('Arbuzik', 12)
    print(p1.get_price_for_qty(2))
    p2r = ProdusLaReducere("Tortik", 120, 25)
    print(p1r.get_price_for_qty(2))
    lista_de_cumparaturi = [
        (p1, 2),
        (p2, 10),
        (p1r, 4),
        (p2r, 1)
    ]
    total = 0
    total_reduceri = 0
    for produs, cantitate in lista_de_cumparaturi:
        total += produs.get_price_for_qty(cantitate)
        if isinstance(produs, ProdusLaReducere):
            total_reduceri += produs.get_reducerea(cantitate)
        # if hasattr(produs, 'get_reducerea'):
        #     total_reduceri += produs.get_reducerea(cantitate)
    print(total)
    print("Redus", total_reduceri)
