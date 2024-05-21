from main import app

from controller.login_controller import *

from model.financiero_model import *

# Menu financiero

@app.route("/menu/financiero")
@app.route("/menu/financiero/page")
@app.route("/menu/financiero/page/<int:page>")
@login_required
def menu_financiero(page=1):
    rows = select_transacciones_db(page)
    return render_template('menu_financiero.html', data=rows)