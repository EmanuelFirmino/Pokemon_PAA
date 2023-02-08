import sqlite3

from database.config import *


class db:

   def __init__(self):

      self.name = './database/pokemon.db'
      self.database = sqlite3.connect(self.name)
      self.cursor = self.database.cursor()

   def get_pokemon(self):

      self.cursor.execute('SELECT * from pokemon')
      return self.cursor.fetchall()

   def disconnect(self):

      self.database.close()


def createDB():

   QNT_POKEMON = 1000
   db = sqlite3.connect('./pokemon.db')
   cursor = db.cursor()

   cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon (id      INTEGER PRIMARY KEY,
                                                          name    CHAR(30),
                                                          weight  INTEGER,
                                                          height  INTEGER,
                                                          experience INTEGER,
                                                          type    CHAR(30),
                                                          sprite  CHAR(200),
                                                          ability1 CHAR(50),
                                                          ord   INTEGER,
                                                          hp      INTEGER,
                                                          attack  INTEGER,
                                                          defense INTEGER,
                                                          ability1_hidden INTEGER,
                                                          ability2 CHAR(50),
                                                          ability2_hidden INTEGER,
                                                          gameVersion CHAR(20),
                                                          gameVersion2 CHAR(20),
                                                          has_female_version INTEGER,
                                                          has_shiny_version INTEGER,
                                                          type2 CHAR(30)
                                                          )
                                                          ''')

   db.commit()

   for pokemon_index in range(1, QNT_POKEMON+1):

      pokemon = getJSON('pokemon/' + str(pokemon_index))

      values = [
          pokemon_index,
          pokemon['name'],
          pokemon['weight'],
          pokemon['height'],
          pokemon['base_experience'],
          pokemon['types'][0]['type']['name'],
          f'./pages/static/sprites/{pokemon_index}.png',
          pokemon['abilities'][0]['ability']['name'],
          pokemon['order'],
          pokemon['stats'][0]['base_stat'],
          pokemon['stats'][1]['base_stat'],
          pokemon['stats'][2]['base_stat'],
          1 if pokemon['abilities'][0]['is_hidden'] else 0,
          pokemon['abilities'][1]['ability']['name'] if len(
              pokemon['abilities']) > 1 else 'none',
          1 if len(pokemon['abilities']
                   ) > 1 and pokemon['abilities'][1]['is_hidden'] else 0,
          pokemon['game_indices'][0]['version']['name'] if len(
              pokemon['game_indices']) else 'none',
          pokemon['game_indices'][1]['version']['name'] if len(
              pokemon['game_indices']) > 1 else 'none',
          1 if pokemon['sprites']['front_female'] else 0,
          1 if pokemon['sprites']['front_shiny'] else 0,
          pokemon['types'][1]['type']['name'] if len(
              pokemon['types']) > 1 else 'none',

      ]

      cursor.execute(
          f'INSERT INTO pokemon VALUES({",".join(["?"] * len(values))})', values)
      db.commit()

      print(f'#Pokemon {pokemon_index} adicionado ao banco de dados!')
