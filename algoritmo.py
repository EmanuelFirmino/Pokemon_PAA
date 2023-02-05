class ALGORITMO:
    
    def __init__(self):
        self.data = None


    def run(self, ans: str, db: dict):

        achou = not (db.get(ans, False)==False)
        question = ''
        if len(ans)==0:
            question = 'Seu Pokemon é leve?(pesa menos que 300 kg)'
        if len(ans)==1:
            question = 'Seu Pokemon é pequeno?(menor que 10 metros)'
        if len(ans)==2:
            question = 'Seu Pokemon é do  tipo  água?'
        if len(ans)==3:
            question = 'Seu Pokemon é do  tipo  normal?'
        if len(ans)==4:
            question = 'Seu Pokemon tem uma defesa fraca?(menor que 70)'
        if len(ans)==5:
            if achou: question = 'Seu Pokemon eh o %s'%(db[ans])
            else: question = 'Nao achei seu Pokemon'
        return question, achou
