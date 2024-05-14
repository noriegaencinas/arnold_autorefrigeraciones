from main import app

from controller.login_controller import *

from model.inventario_model import *

# Menu inventario

@app.route("/menu/inventario")
@app.route("/menu/inventario/page")
@app.route("/menu/inventario/page/<int:page>")
@login_required
def menu_inventario(page=1):
    rows = select_inventario_db(page)
    return render_template('menu_inventario.html', data=rows)