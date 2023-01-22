from database.config import *
import sqlite3

class db:

    def __init__(self):

        self.name     = './database/pokemon.db'
        self.database = sqlite3.connect(self.name)
        self.cursor   = self.database.cursor() 

    def get_pokemon(self):

        self.cursor.execute('SELECT * from pokemon')
        return self.cursor.fetchall()

    def disconnect(self):

        self.database.close()

def createDB():

    QNT_POKEMON = 1000
    db          = sqlite3.connect('./pokemon.db')
    cursor      = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon (id      INTEGER PRIMARY KEY,
                                                          name    CHAR(30),
                                                          weight  INTEGER,
                                                          height  INTEGER,
                                                          experience INTEGER,
                                                          type    CHAR(30),
                                                          sprite  CHAR(200),
                                                          ability CHAR(50),
                                                          ord   INTEGER,
                                                          hp      INTEGER,
                                                          attack  INTEGER,
                                                          defense INTEGER
                                                          )
                                                          ''')

    db.commit()

    for pokemon_index in range(1, QNT_POKEMON):

        pokemon = getJSON(pokemon_index)

        values  = [ 
                    pokemon_index,
                    pokemon['name'],
                    pokemon['weight'],
                    pokemon['height'],
                    pokemon['base_experience'],
                    pokemon['types'][0]['type']['name'],
                    f'./database/sprites/{pokemon_index}.png',
                    pokemon['abilities'][0]['ability']['name'],
                    pokemon['order'],
                    pokemon['stats'][0]['base_stat'],
                    pokemon['stats'][1]['base_stat'],
                    pokemon['stats'][2]['base_stat']
                  ]

        cursor.execute('INSERT INTO pokemon VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)
        db.commit()

        print(f'#Pokemon {pokemon_index} adicionado ao banco de dados!')