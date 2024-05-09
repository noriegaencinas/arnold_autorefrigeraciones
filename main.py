# Imports for Flask
from flask import Flask

# Inicializando aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'miguelito'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arnold_autorefrigeraciones.db'

from controller.controllers import *

if __name__ == '__main__':
    app.run(debug=True, port=5005)
