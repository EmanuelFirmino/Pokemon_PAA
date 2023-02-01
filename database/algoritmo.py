import numpy as np
import pandas as pd

from database import db

data = db()
pokemons = data.get_pokemon()

lista_pokemons = list()
for i in range(len(pokemons)):
   lista_pokemons.append(list(pokemons[i]))

lista_pokemons = pd.DataFrame(lista_pokemons)

# print(lista_pokemons.shape)
# print(lista_pokemons.describe())
pesos = lista_pokemons[2]
alturas = lista_pokemons[3]
tipes = lista_pokemons[5]
abilits = lista_pokemons[7]
defense = lista_pokemons[11]
# xp = lista_pokemons[4]
# print(defense)
# print(defense.describe())
# print(defense.value_counts(dropna=True))

lista_perguntas = pd.DataFrame()
lista_perguntas['Seu Pokemon é leve?(pesa menos que 300 kg)'] = np.where(
    lista_pokemons[2] < 300, 1, 0)
lista_perguntas['Seu Pokemon é pequeno?(menor que 10 metros)'] = np.where(
    lista_pokemons[3] < 10, 1, 0)
lista_perguntas['Seu Pokemon é do  tipo  água?'] = np.where(
    lista_pokemons[5] == 'water', 1, 0)
lista_perguntas['Seu Pokemon é do  tipo  normal?'] = np.where(
    lista_pokemons[5] == 'normal', 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa fraca?(menor que 70)'] = np.where(
    lista_pokemons[11] < 70, 1, 0)

# print(lista_perguntas['Seu Pokemon tem uma defesa fraca?(menor que 70)'].value_counts())
contagem = lista_perguntas.value_counts()
# lista_perguntas['contador'] = contagem
print(contagem)
