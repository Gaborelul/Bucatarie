import pickle
import json
from src.bucatarie import Bucatarie
from src.reteta import Reteta

ingrediente = [{'nume': 'oua', 'cantitate': 4},
               {'nume': 'faina', 'cantitate': 400},
               {'nume': 'lapte', 'cantitate': 500},
               {'nume': 'zahar', 'cantitate': 100},
               {'nume': 'bicarbonat', 'cantitate': 10},
               {'nume': 'praf_de_copt', 'cantitate': 30},
               {'nume': 'ulei', 'cantitate': 120}]
Tort_cu_ciocolata=[
  {"nume": "oua", "cantitate": 6},
  {"nume": "faina", "cantitate": 500},
  {"nume": "zahar", "cantitate": 200},
  {"nume": "ciocolata", "cantitate": 200}]

bucatarie= Bucatarie()

reteta=Reteta('Clatite',ingrediente)
reteta.pregatire(bucatarie)

reteta_tort=Reteta('Tort cu ciocolata', Tort_cu_ciocolata)
reteta.pregatire(bucatarie)


retete_folosite=[]
retete_folosite.append(reteta)
retete_folosite.append(reteta_tort)
# print(retete_folosite[0].nume,'\n')



with open('data/my_object.pickle', 'wb') as f:
    pickle.dump(retete_folosite, f)

with open('data/my_object.pickle', 'rb') as f:
    loaded_object = pickle.load(f)

print(retete_folosite[0].nume,'\n')
print(loaded_object[0].ingrediente,'\n')

print(retete_folosite[1].nume)
print(loaded_object[1].ingrediente,'\n')

with open('data/Inventar.json', 'r') as file:
    d = json.load(file)
    print(d)

# {"faina": 5000, "lapte": 3000, "oua": 300, "praf_de_copt": 400, "bicarbonat": 300, "zahar": 1000, "ulei": 1000}
