import json

class Bucatarie:
    def __init__(self):
        with open("data/Inventar.json") as f:
            self.inventar = json.load(f)

    def adauga_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar:
            self.inventar[nume_produs] += cantitate
        else:
            self.inventar[nume_produs] = cantitate

        with open("data/Inventar.json", "w") as f:
            json.dump(self.inventar, f)

    def scadere_produs(self, nume_produs, cantitate):
        if nume_produs in self.inventar:
            if self.inventar[nume_produs] >= cantitate:
                self.inventar[nume_produs] -= cantitate
            else:
                print("Nu exista suficient {} in inventar.".format(nume_produs))
        else:
            print("Ingredientul {} nu exista in inventar.".format(nume_produs))


        with open("data/Inventar.json", "w") as f:
            json.dump(self.inventar, f)










