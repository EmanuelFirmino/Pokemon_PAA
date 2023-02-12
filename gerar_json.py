from json import dump

from database.database import db

'''
lista_perguntas['Seu Pokemon é novo?(ordem da Pokédex maior que 580)'] = np.where(
    lista_pokemons[8] > 580, 1, 0)
lista_perguntas['Seu Pokemon é muito novo?(ordem da Pokédex maior que 880)'] = np.where(
    lista_pokemons[8] > 880, 1, 0)
lista_perguntas['Seu Pokemon é muito velho?(ordem da Pokédex menor que 300)'] = np.where(
    lista_pokemons[8] < 300, 1, 0)
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
lista_perguntas['Seu Pokemon tem uma defesa muito fraca?(menor que 51)'] = np.where(
    lista_pokemons[11] < 51, 1, 0)
lista_perguntas['Seu Pokemon tem uma defesa muito forte?(maior que 89)'] = np.where(
    lista_pokemons[11] > 89, 1, 0)
lista_perguntas['Seu Pokemon é muito pequeno?(menor que 6 metros)'] = np.where(
    lista_pokemons[3] < 6, 1, 0)
lista_perguntas['Seu Pokemon é muito grande?(maior que 15 metros)'] = np.where(
    lista_pokemons[3] > 15, 1, 0)
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
lista_perguntas['Seu Pokemon tem xp muito alta?(maior que 180)'] = np.where(
    lista_pokemons[4] > 180, 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Black and White?'] = np.where(
    lista_pokemons[15] == 'black', 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Red?'] = np.where(
    lista_pokemons[15] == 'red', 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Ruby and Sapphire?'] = np.where(
    lista_pokemons[15] == 'ruby', 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game Pokémon Diamond and Pearl?'] = np.where(
    lista_pokemons[15] == 'diamond', 1, 0)
lista_perguntas['Seu Pokemon aparece pela primeira vez no game pokemon Gold and Silver?'] = np.where(
    lista_pokemons[15] == 'gold', 1, 0)
lista_perguntas['Seu Pokemon possui habilidade de flying, poison, psychic, ou ground?'] = np.where(
    lista_pokemons[19].isin(['flying', 'poison', 'psychic', 'ground']), 1, 0)
'''


ls = db().get_pokemon()
dc = {e[1]: str() for e in ls}
for i in range(len(ls)):
   dc[ls[i][1]] += '1' if ls[i][2] < 300 else '0'

for i in range(len(ls)):
   dc[ls[i][1]] += '1' if ls[i][3] < 10 else '0'

for i in range(len(ls)):
   dc[ls[i][1]] += '1' if ls[i][5] == 'water' else '0'

for i in range(len(ls)):
   dc[ls[i][1]] += '1' if ls[i][5] == 'normal' else '0'

for i in range(len(ls)):
   dc[ls[i][1]] += '1' if ls[i][11] < 70 else '0'

dc2 = dict()

for k in dc:
   dc2[dc[k]] = k

with open('db.json', 'w+') as f:
   dump(dc2, f, indent=4)
