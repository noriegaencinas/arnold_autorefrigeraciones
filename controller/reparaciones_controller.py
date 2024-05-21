from main import app

from controller.login_controller import *

from model.reparaciones_model import *

# Menu reparaciones

@app.route("/menu/reparaciones")
@app.route("/menu/reparaciones/page")
@app.route("/menu/reparaciones/page/<int:page>")
@login_required
def registro_reparaciones(page=1):
    rows = select_automovil_db(page)
    return render_template('menu_reparaciones.html', data=rows)

@app.route("/menu/reparaciones/buscar", methods=['GET', 'POST'])
@login_required
def select_reparacion_by_filter():
    if request.method == 'POST':
        filtro = request.form['filtro']
        rows = select_automovil_by_filter_db(filtro)
        return render_template('menu_reparaciones.html', data=rows)
    return redirect(url_for('registro_reparaciones'))

@app.route("/menu/reparaciones/activar/<int:id_automovil>", methods=['GET', 'POST'])
def activar_automovil(id_automovil):
    if request.method == 'POST':
        activar_automovil_db(id_automovil)
        return redirect(url_for('registro_reparaciones'))
    return redirect(url_for('registro_reparaciones'))