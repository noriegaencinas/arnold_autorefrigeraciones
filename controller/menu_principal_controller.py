from main import app

from controller.login_controller import *

# Menu prinicipal

@app.route("/menu")
@login_required
def menu():
    return render_template('menu.html')