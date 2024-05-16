from main import app

from controller.login_controller import *
from controller.cliente_controller import *

from model.factura_model import *

# Menu facturas

@app.route("/menu/facturas")
@login_required
def menu_facturas():
    options = select_clientes_db()
    return render_template('menu_facturas.html', cliente_options=options)