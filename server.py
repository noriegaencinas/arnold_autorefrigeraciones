from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/sign-in")
def index():
    return render_template('sign-in.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/menu/inventario")
def menu_inventario():
    return render_template('menu_inventario.html')

@app.route("/menu/automoviles")
def menu_automoviles():
    return render_template('menu_automoviles.html')

@app.route("/menu/empleados")
def menu_empleados():
    return render_template('menu_empleados.html')

@app.route("/menu/financiero")
def menu_financiero():
    return render_template('menu_financiero.html')

@app.route("/menu/facturas")
def menu_facturas():
    return render_template('menu_facturas.html')

if __name__ == '__main__':
    app.run(debug=True, port=5004)