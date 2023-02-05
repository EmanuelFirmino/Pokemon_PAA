from random import randint
from flask import Flask, render_template, request
from database import database
from algoritmo import *

class PAA:

   def __init__(self):

      self.algoritmo = ALGORITMO()
      self.app = Flask(__name__, template_folder='./pages/html', static_folder='./pages/static')
      self.routes()

   def routes(self):

      @self.app.route('/', methods=['GET', 'POST'])

      def index():

         sprite = f'../static/assets/g.gif'
         question = 'Menu'
         find_it = False

         if request.method == 'POST':

            response = request.get_data().decode()[:-1]

            if    response == 'positive':
               response = 1
            elif  response == 'negative':
               response = -1
            else:
               response = 0

            result = self.algoritmo.run(response)

            find_it  = result[1]
            question = result[0]

         return render_template('index.html', title="Home", question=question, sprite=sprite, find_it=find_it)

   def start(self):

      self.app.run(debug=True)


App = PAA()

if __name__ == '__main__':
   App.start()
