class ALGORITMO:
    
    def __init__(self):
        self.data = None


    def run(self, ans: str, db: dict):

        achou = not (db.get(ans, False)==False)
        question = ''

        match len(ans):
            case 0:
                question = 'Seu Pokemon é leve?(pesa menos que 30 kg)'
            case 1:
                question = 'Seu Pokemon é pequeno?(menor que 1 metro)'
            case 2:
                question = 'Seu Pokemon tem pouca vida? (menor que 66)'
            case 3:
                question = 'Seu Pokemon tem um ataque fraco? (menor que 75)'
            case 4:
                question = 'Seu Pokemon tem uma defesa fraca? (menor que 70)'
            case 5:
                question = 'Seu Pokemon solta raios?'
            case 3:
                question = 'Seu Pokemon parece uma planta?'
            case 4:
                question = 'Seu Pokemon é do tipo água?'
            case 5:
                question = 'Seu Pokemon solta fogo?'
            case 6:
                question = 'Seu Pokemon se parece com um inseto?'
            case 7:
                question = 'Seu Pokemon possui asas?'
            case 8:
                question = 'Seu Pokemon é do tipo normal?'
            case 9:
                question = 'Seu Pokemon é venenoso?'
            case 10:
                if achou: question = 'Seu Pokemon eh o %s'%(db[ans])
                else: question = 'Nao achei seu Pokemon'
        return question, achou
