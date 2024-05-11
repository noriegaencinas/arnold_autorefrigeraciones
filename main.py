# Imports for Flask
from flask import Flask

# Inicializando aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'miguelito'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arnold_autorefrigeraciones.db'

from controller.menu_principal_controller import *
from controller.inventario_controller import *
from controller.automovil_controller import *
from controller.financiero_controller import *
from controller.empleado_controller import *
from controller.reparaciones_controller import *
from controller.factura_controller import *


if __name__ == '__main__':
    app.run(debug=True, port=5005)
