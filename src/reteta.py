class Reteta:
    def __init__(self, nume, ingrediente):
        self.nume = nume
        self.ingrediente = ingrediente

    def pregatire(self, bucatarie):
        for ingredient in self.ingrediente:
            bucatarie.scadere_produs(ingredient['nume'], ingredient['cantitate'])










