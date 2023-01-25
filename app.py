from flask import Flask, render_template, request
from database import database
from random import randint

class PAA:

    def __init__(self):

        self.questions = ['O seu Pokémon é do tipo Fogo?', 'O seu Pokémon é quadrúpede?', 'O seu pokémon pesa mais de 64kg?']
        self.curr_question = 2
        self.app = Flask(__name__, template_folder='./pages/html', static_folder='./pages/static')
        self.routes()

    def routes(self):

        @self.app.route('/', methods=['GET', 'POST'])
        def index():

            sprite = f'../static/assets/pikachu{randint(1, 5)}.png'

            if request.method == 'POST':
                self.curr_question = (self.curr_question + 1) % len(self.questions)
                    
            return render_template('index.html', title="Home", question=self.questions[self.curr_question], sprite=sprite)

    def start(self):

        self.app.run(debug=True)

App = PAA()

if __name__ == '__main__':
    App.start()