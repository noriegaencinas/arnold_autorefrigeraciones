from main import app

from controller.login_controller import *

from model.reparaciones_model import *

# Menu reparaciones

@app.route("/menu/reparaciones")
@login_required
def registro_reparaciones():
    rows = SelectRegistroReparaciones()
    return render_template('menu_reparaciones.html', reparaciones=rows)