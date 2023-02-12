import numpy as np
import pandas as pd

from database.database import db

data = db()
pokemons = data.get_pokemon()

lista_pokemons = list()
for i in range(len(pokemons)):
   lista_pokemons.append(list(pokemons[i]))

lista_pokemons = pd.DataFrame(lista_pokemons)


lista_perguntas = pd.DataFrame()

lista_perguntas['Pokémon'] = lista_pokemons[1]
lista_perguntas['Sprite'] = lista_pokemons[6]
lista_perguntas['Seu Pokemon possui dois tipos?'] = np.where(
    lista_pokemons[19] == 'none', 0, 1)
lista_perguntas['Seu Pokemon tem uma defesa fraca?(menor que 70)'] = np.where(
    lista_pokemons[11] < 70, 1, 0)
lista_perguntas['Seu Pokemon tem xp alta?(maior que 145)'] = np.where(
    lista_pokemons[4] > 145, 1, 0)
lista_perguntas['Seu Pokemon é novo?(ordem da Pokédex maior que 580)'] = np.where(
    lista_pokemons[8] > 580, 1, 0)
lista_perguntas['Seu Pokemon é pequeno?(menor que 10 metros)'] = np.where(
    lista_pokemons[3] < 10, 1, 0)
lista_perguntas['Seu Pokemon é leve?(pesa menos que 300 kg)'] = np.where(
    lista_pokemons[2] < 300, 1, 0)
lista_perguntas['Seu Pokemon tem ataque forte?(maior que 77)'] = np.where(
    lista_pokemons[10] > 77, 1, 0)
lista_perguntas['Seu Pokemon tem bom hp?(maior que 70)'] = np.where(
    lista_pokemons[9] > 70, 1, 0)
lista_perguntas['Seu Pokemon tem Hidden Abilities 2?'] = lista_pokemons[14]
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Black ou Red?'] = np.where(
    lista_pokemons[15].isin(['black', 'red']), 1, 0)
lista_perguntas['Seu Pokemon tem pouco hp?(menor que 55)'] = np.where(
    lista_pokemons[9] < 55, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa muito fraca?(menor que 51)'] = np.where(
    lista_pokemons[11] < 51, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa muito forte?(maior que 89)'] = np.where(
    lista_pokemons[11] > 89, 1, 0)
lista_perguntas['Seu Pokemon é muito novo?(ordem da Pokédex maior que 880)'] = np.where(
    lista_pokemons[8] > 880, 1, 0)
lista_perguntas['Seu Pokemon tem xp muito baixa?(menor que 70)'] = np.where(
    lista_pokemons[4] < 70, 1, 0)
lista_perguntas['Seu Pokemon é muito pequeno?(menor que 6 metros)'] = np.where(
    lista_pokemons[3] < 6, 1, 0)
lista_perguntas['Seu Pokemon tem ataque muito forte?(maior que 99)'] = np.where(
    lista_pokemons[10] > 99, 1, 0)
lista_perguntas['Seu Pokemon é do  tipo  água ou normal?'] = np.where(
    lista_pokemons[5].isin(['water', 'normal']), 1, 0)
lista_perguntas['Seu Pokemon é muito velho?(ordem da Pokédex menor que 300)'] = np.where(
    lista_pokemons[8] < 300, 1, 0)
lista_perguntas['Seu Pokemon tem ataque muito fraco?(menor que 10)'] = np.where(
    lista_pokemons[10] < 55, 1, 0)

df = pd.DataFrame(lista_perguntas)

# Salvando o DataFrame como um arquivo Excel
df.to_excel("df_pandas_to_excel.xlsx", index=False)

# print(lista_perguntas.head())
# lista_perguntas['Seu Pokemon é muito grande?(maior que 15 metros)'] = np.where(lista_pokemons[3] > 15, 1, 0)


# all_values = lista_perguntas.value_counts().values.flatten()
# freq = pd.Series(all_values)
# freq = (freq == 1, 1, 0)
# print((freq == 1).value_counts())
# freq = (freq != 1)
# print(freq.value_counts())
# print(lista_perguntas.shape)
'''
lista_perguntas['Seu Pokemon é muito novo?(ordem da Pokédex maior que 880)'] = np.where(
    lista_pokemons[8] > 880, 1, 0)
lista_perguntas['Seu Pokemon é muito velho?(ordem da Pokédex menor que 300)'] = np.where(
    lista_pokemons[8] < 300, 1, 0)
lista_perguntas['Seu Pokemon é leve?(pesa menos que 300 kg)'] = np.where(
    lista_pokemons[2] < 300, 1, 0)
lista_perguntas['Seu Pokemon é muito leve?(pesa menos que 50 kg)'] = np.where(
    lista_pokemons[2] < 50, 1, 0)
lista_perguntas['Seu Pokemon é muito pesado?'] = np.where(
    lista_pokemons[2] > 1000, 1, 0)
lista_perguntas['Seu Pokemon tem muito hp(maior que 99)'] = np.where(
    lista_pokemons[9] > 99, 1, 0)
lista_perguntas['Seu Pokemon tem bom hp?(maior que 70)'] = np.where(
    lista_pokemons[9] > 70, 1, 0)
lista_perguntas['Seu Pokemon tem pouco hp?(menor que 55)'] = np.where(
    lista_pokemons[9] < 55, 1, 0)
lista_perguntas['Seu Pokemon tem ataque muito forte?(maior que 99)'] = np.where(
    lista_pokemons[10] > 99, 1, 0)
lista_perguntas['Seu Pokemon tem ataque forte?(maior que 77)'] = np.where(
    lista_pokemons[10] > 77, 1, 0)
lista_perguntas['Seu Pokemon tem ataque muito fraco?(menor que 10)'] = np.where(
    lista_pokemons[10] < 55, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa fraca?(menor que 70)'] = np.where(
    lista_pokemons[11] < 70, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa muito fraca?(menor que 51)'] = np.where(
    lista_pokemons[11] < 51, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa muito forte?(maior que 89)'] = np.where(
    lista_pokemons[11] > 89, 1, 0)
lista_perguntas['Seu Pokemon é pequeno?(menor que 10 metros)'] = np.where(
    lista_pokemons[3] < 10, 1, 0)
lista_perguntas['Seu Pokemon é muito pequeno?(menor que 6 metros)'] = np.where(
    lista_pokemons[3] < 6, 1, 0)
lista_perguntas['Seu Pokemon é muito grande?(maior que 15 metros)'] = np.where(
    lista_pokemons[3] > 15, 1, 0)
lista_perguntas['Seu Pokemon é do  tipo  água?'] = np.where(
    lista_pokemons[5] == 'water', 1, 0)
lista_perguntas['Seu Pokemon é do  tipo  normal?'] = np.where(
    lista_pokemons[5] == 'normal', 1, 0)
lista_perguntas['Seu Pokemon é do  tipo fogo?'] = np.where(
    lista_pokemons[5] == 'fire', 1, 0)
lista_perguntas['Seu Pokemon tem Hidden Abilities 2?'] = lista_pokemons[14]
lista_perguntas['Seu Pokemon tem versão feminina?'] = lista_pokemons[17]
lista_perguntas['Seu Pokemon tem versão Shiny?'] = lista_pokemons[18]
lista_perguntas['Seu Pokemon possui dois tipos?'] = np.where(
    lista_pokemons[19] == 'none', 0, 1)
lista_perguntas['Seu Pokemon tem xp alta?(maior que 145)'] = np.where(
    lista_pokemons[4] > 145, 1, 0)
lista_perguntas['Seu Pokemon tem xp muito baixa?(menor que 70)'] = np.where(
    lista_pokemons[4] < 70, 1, 0)
#lista_perguntas['Seu Pokemon tem xp muito alta?(maior que 180)'] = np.where(lista_pokemons[4] > 180, 1, 0)
lista_perguntas['Seu Pokemon tem xp muito alta?(maior que 180)'] = np.where(
    lista_pokemons[4] > 180, 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Black ou Red?'] = np.where(
    lista_pokemons[15].isin(['black','red']), 1, 0)

#lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Red?'] = np.where(lista_pokemons[15] == 'red', 1, 0)
#lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Ruby and Sapphire?'] = np.where(lista_pokemons[15] == 'ruby', 1, 0)
#lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Diamond and Pearl?'] = np.where(lista_pokemons[15] == 'diamond', 1, 0)
#lista_perguntas['Seu Pokemon aparece pela primeira vez no game pokemon Gold and Silver?'] = np.where(lista_pokemons[15] == 'gold', 1, 0)
#lista_perguntas['Seu Pokemon possui habilidade de flying, poison, psychic, ou ground?'] = np.where(lista_pokemons[19].isin(['flying', 'poison', 'psychic', 'ground']), 1, 0)

best_questions = {}
for column, value_count in lista_perguntas.items():
   value_count = pd.DataFrame(value_count.value_counts())
   best_questions = (value_count.diff()).dropna()
# for values in best_questions.values():
#print(best_questions)
# print(best_questions)
# best_questions = pd.concat(best_questions, axis=1)
# print(best_questions)
# best_questions = best_questions.abs().sum(axis=1).sort_values()
# print(best_questions)
'''
'''
# Loop over the columns and get the value counts for each column
best_questions = {}
for column, value_count in lista_perguntas.items():
   # print("Value counts of", column + ":")
   best_questions[column] = (value_count.value_counts()).diff()
   # print("\n")
best_questions = best_questions.abs().sum(axis=1).sort_values()
print(best_questions)



all_values = lista_perguntas.value_counts().values.flatten()
freq = pd.Series(all_values)
# freq = (freq == 1, 1, 0)
# print((freq == 1).value_counts())
freq = (freq != 1)
# print(freq.value_counts())
print(lista_perguntas.shape)'''
