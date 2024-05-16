from main import app

from controller.login_controller import *

from model.cliente_model import *

@app.route("/menu/cliente/agregar", methods=['GET', 'POST'])
@login_required
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre_completo']
        correo = request.form['correo_electronico']
        telefono = request.form['telefono']
        agregar_cliente_db(nombre, telefono, correo)
        return redirect(url_for('menu_facturas'))
    return redirect(url_for('menu_facturas'))
    
