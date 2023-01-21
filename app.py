from flask import Flask, render_template, request
from config import *

class PAA:

    def __init__(self):

        self.app = Flask(__name__, template_folder='./pages/html', static_folder='./pages/static')
        self.routes()
        self.app.run(debug=True)

    def routes(self):

        @self.app.route('/')
        def index():
            return render_template('index.html', title="Home")

if __name__ == '__main__':
    PAA()