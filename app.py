from flask import Flask, render_template, request
from database import database

class PAA:

    def __init__(self):

        self.app = Flask(__name__, template_folder='./pages/html', static_folder='./pages/static')
        self.routes()

    def routes(self):

        @self.app.route('/')
        def index():
            return render_template('index.html', title="Home")

    def start(self):

        self.app.run(debug=True)

App = PAA()

if __name__ == '__main__':
    App.start()