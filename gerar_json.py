from json import dump
from database.database import db

#        # print(lista_pokemons.shape)
#        # print(lista_pokemons.describe())
#        pesos = lista_pokemons[2]
#        alturas = lista_pokemons[3]
#        tipes = lista_pokemons[5]
#        abilits = lista_pokemons[7]
#        defense = lista_pokemons[11]
#        # xp = lista_pokemons[4]
#        # print(defense)
#        # print(defense.describe())
#        # print(defense.value_counts(dropna=True))
#
#
#    lista_perguntas = pd.DataFrame()
#        lista_perguntas['Seu Pokemon é leve?(pesa menos que 300 kg)'] = np.where(
#            lista_pokemons[2] < 300, 1, 0)
#        lista_perguntas['Seu Pokemon é pequeno?(menor que 10 metros)'] = np.where(
#            lista_pokemons[3] < 10, 1, 0)
#        lista_perguntas['Seu Pokemon é do  tipo  água?'] = np.where(
#            lista_pokemons[5] == 'water', 1, 0)
#        lista_perguntas['Seu Pokemon é do  tipo  normal?'] = np.where(
#            lista_pokemons[5] == 'normal', 1, 0)
#        lista_perguntas['Seu Pokemon tem uma defesa fraca?(menor que 70)'] = np.where(
#            lista_pokemons[11] < 70, 1, 0)


ls = db().get_pokemon()
dc = {e[1]:str() for e in ls}
for i in range(len(ls)): dc[ls[i][1]] += '1' if ls[i][2]<300 else '0'

for i in range(len(ls)): dc[ls[i][1]] += '1' if ls[i][3]<10 else '0'

for i in range(len(ls)): dc[ls[i][1]] += '1' if ls[i][5]=='water' else '0'

for i in range(len(ls)): dc[ls[i][1]] += '1' if ls[i][5]=='normal' else '0'

for i in range(len(ls)): dc[ls[i][1]] += '1' if ls[i][11]<70 else '0'

dc2 = dict()

for k in dc: dc2[dc[k]] = k

with open('db.json', 'w+') as f: dump(dc2, f, indent=4)
