class ALGORITMO:

   def __init__(self):
      self.data = None

   def run(self, ans: str, db: dict):

      achou = not (db.get(ans, False) == False)
      question = ''
      if len(ans) == 0:
         question = 'Seu Pokemon é leve?(pesa menos que 300 kg)'
      if len(ans) == 1:
         question = 'Seu Pokemon é pequeno?(menor que 10 metros)'
      if len(ans) == 2:
         question = 'Seu Pokemon é do  tipo  água?'
      if len(ans) == 3:
         question = 'Seu Pokemon é do  tipo  normal?'
      if len(ans) == 4:
         question = 'Seu Pokemon tem uma defesa fraca?(menor que 70)'
      if len(ans) == 5:
         question = 'Seu Pokemon é novo?(ordem da Pokédex maior que 580)'
      if len(ans) == 6:
         question = 'Seu Pokemon tem bom hp?(maior que 70)'
      if len(ans) == 7:
         question = 'Seu Pokemon tem ataque forte?(maior que 77)'
      if len(ans) == 8:
         question = 'Seu Pokemon possui dois tipos?'
      if len(ans) == 9:
         question = 'Seu Pokemon tem xp alta?(maior que 145)'
      if len(ans) == 10:
         question = 'Seu Pokemon tem Hidden Abilities 2?'
      if len(ans) == 11:
         question = 'Seu Pokemon é muito novo?(ordem da Pokédex maior que 880)'
      if len(ans) == 12:
         question = 'Seu Pokemon aparece pela primeira vez no game pokemon Gold and Silver?'
      if len(ans) == 13:
         question = 'Seu Pokemon é muito leve?(pesa menos que 50 kg)'
      if len(ans) == 14:
         question = 'Seu Pokemon é muito velho?(ordem da Pokédex menor que 300)'
      if len(ans) == 15:
         question = 'Seu Pokemon é muito pesado?'
      if len(ans) == 16:
         question = 'Seu Pokemon aparece pela primeira vez no game Pokémon Diamond and Pearl?
      if len(ans) == 17:
         question = 'Seu Pokemon tem pouco hp?(menor que 55)'
      if len(ans) == 18:
         question = 'Seu Pokemon tem uma defesa muito fraca?(menor que 51)'
      if len(ans) == 19:
         question = 'Seu Pokemon tem ataque muito fraco?(menor que 10)'
      if len(ans) == 20:
         question = 'Seu Pokemon aparece pela primeira vez no game Pokémon Red?
      if len(ans) == 21:
         question = 'Seu Pokemon aparece pela primeira vez no game Pokémon Black and White?'
      if len(ans) == 22:
         question = 'Seu Pokemon tem muito hp(maior que 99)'
      if len(ans) == 23:
         question = 'Seu Pokemon aparece pela primeira vez no game Pokémon Ruby and Sapphire?'
      if len(ans) == 24:
         question = 'Seu Pokemon tem ataque muito forte?(maior que 99)'
      if len(ans) == 25:
         question = 'Seu Pokemon possui habilidade de flying, poison, psychic, ou ground?'
      if len(ans) == 25:
         question = 'Seu Pokemon tem xp muito alta?(maior que 180)'
      if len(ans) == 26:
         question = 'Seu Pokemon tem xp muito baixa?(menor que 70)'
      if len(ans) == 27:
         question = 'Seu Pokemon é muito grande?(maior que 15 metros)'
      if len(ans) == 28:
         question = 'Seu Pokemon é do  tipo fogo?'
      if len(ans) == 29:
         question = 'Seu Pokemon tem uma defesa muito forte?(maior que 89)'
      if len(ans) == 30:
         question = 'Seu Pokemon é muito pequeno?(menor que 6 metros)'
      if len(ans) == 31:
         question = 'Seu Pokemon tem versão feminina?'
      if len(ans) == 32:
         question = 'Seu Pokemon tem versão Shiny?'
      if len(ans) == 33:
         if achou:
            question = 'Seu Pokemon eh o %s' % (db[ans])
         else:
            question = 'Nao achei seu Pokemon'
      return question, achou
