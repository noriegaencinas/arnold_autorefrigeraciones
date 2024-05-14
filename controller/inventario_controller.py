from main import app

from controller.login_controller import *

from model.inventario_model import *

# Menu inventario

@app.route("/menu/automoviles")
@app.route("/menu/automoviles/page")
@app.route("/menu/automoviles/page/<int:page>")
@login_required
def menu_automoviles(page=1):
    rows = select_inventario_db(page)
    return render_template('menu_inventario.html', data=rows)