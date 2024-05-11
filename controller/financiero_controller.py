from main import app

from controller.login_controller import *

from model.financiero_model import *

# Menu financiero

@app.route("/menu/financiero")
@login_required
def menu_financiero():
    return render_template('menu_financiero.html')
