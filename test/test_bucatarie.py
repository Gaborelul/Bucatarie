import json

class Bucatarie:
    def __init__(self, nume, inventar_path):
        self.nume = nume
        with open(inventar_path, 'r') as f:
            inventar_data = json.load(f)
            self.inventar = inventar_data

    def adauga_ingredient(self, nume_ingredient, cantitate):
        if nume_ingredient in self.inventar:
            self.inventar[nume_ingredient] += cantitate
        else:
            self.inventar[nume_ingredient] = cantitate

    def scade_ingredient(self, nume_ingredient, cantitate):
        if nume_ingredient in self.inventar:
            if self.inventar[nume_ingredient] >= cantitate:
                self.inventar[nume_ingredient] -= cantitate
            else:
                raise ValueError("Nu exista suficient " + nume_ingredient + " in inventar!")
        else:
            raise ValueError(nume_ingredient + " nu exista in inventar!")

class Reteta:
    def __init__(self, reteta_path):
        with open(reteta_path, 'r') as f:
            reteta_data = json.load(f)
            self.nume = reteta_data["nume"]
            self.ingrediente = reteta_data["ingrediente"]
class ProdusFinal(Reteta):
    def __init__(self, reteta_path, bucatarie):
        super().__init__(reteta_path)
        self.bucatarie = bucatarie
        self.ingrediente_utilizate = []
        for ingred in self.ingrediente:
            nume_ingred = ingred["ingredient"]
            cantitate = ingred["cantitate"]
            self.bucatarie.scade_ingredient(nume_ingred, cantitate)
            self.ingrediente_utilizate.append(nume_ingred)

    def adauga_la_produse_finale(self, produse_finale):
        produse_finale.append(self)

# Creaza un obiect de tip Bucatarie si afiseaza inventarul initial
bucatarie = Bucatarie("Bucataria mea", "inventar.json")
print("Inventar initial:", bucatarie.inventar)

# Adauga ingrediente in inventar si afiseaza noul inventar
bucatarie.adauga_ingredient("ciocolata", 200)
bucatarie.adauga_ingredient("mere", 6)
print("Inventar dupa adaugarea de ingrediente:", bucatarie.inventar)

# Creeaza un obiect de tip ProdusFinal pentru reteta1 si adauga-l la lista de produse finale
produs1 = ProdusFinal("reteta1.json", bucatarie)
produse_finale = []
produs1.adauga_la_produse_finale(produse_finale)
print("Ingrediente utilizate pentru produsul 1:", produs1.ingrediente_utilizate)
print("Inventar dupa crearea produsului 1:", bucatarie.inventar)
print("Lista de produse finale:")
for produs in produse_finale:
    print(produs.nume)