from main import app

from controller.login_controller import *

from model.inventario_model import *

# Menu inventario

@app.route("/menu/inventario")
@login_required
def menu_inventario():
    return 'Inventario'