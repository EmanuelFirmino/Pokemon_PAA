from flask import Flask, render_template, request
from database import database
from random import randint
def binary_tree(answer: list, tree: dict):
    return tree[''.join(['1' if e else '0' for e in answer])]

class PAA:

    def __init__(self):

        self.questions = ['O seu Pokémon é do tipo Fogo?', 'O seu Pokémon é quadrúpede?', 'O seu pokémon pesa mais de 64kg?']
        self.answers = [False]*len(self.questions)
        self.tree = {'111':'pikachu'}
        self.curr_question = 0
        self.app = Flask(__name__, template_folder='./pages/html', static_folder='./pages/static')
        self.routes()

    def routes(self):

        @self.app.route('/', methods=['GET', 'POST'])
        def index():

            sprite = f'../static/assets/pikachu{randint(1, 5)}.png'
            if request.method == 'POST':
                self.answers[self.curr_question] = request.form.get('positive')!=None
                self.curr_question+=1
            if self.curr_question < len(self.questions):
                return render_template('index.html', title="Home", question=self.questions[self.curr_question], sprite=sprite)
            else:
                self.curr_question = 0
                return render_template('index.html', title="Home", question="O pokemon eh o %s"%(binary_tree(self.answers,self.tree)), sprite=sprite)
    def start(self):

        self.app.run(debug=True)

App = PAA()

if __name__ == '__main__':
    App.start()
