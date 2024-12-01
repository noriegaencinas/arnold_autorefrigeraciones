from main import app

from controller.login_controller import *

from model.factura_empleado_model import *

# Menu facturas

@app.route("/menu/facturacion")
@login_required
def menu_facturas_empleados():
    return render_template('menu_facturas_empleados.html')