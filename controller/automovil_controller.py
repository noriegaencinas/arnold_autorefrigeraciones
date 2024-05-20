from main import app

from controller.login_controller import *

from model.automovil_model import *

# Menu empelados

@app.route("/menu/automoviles")
@app.route("/menu/automoviles/page")
@app.route("/menu/automoviles/page/<int:page>")
@login_required
def menu_automoviles(page=1):
    rows = select_automovil_db(page)
    return render_template('menu_automoviles.html', data=rows)

@app.route("/menu/automoviles/buscar", methods=['GET', 'POST'])
@login_required
def select_automovil_by_filter():
    if request.method == 'POST':
        filtro = request.form['filtro']
        rows = select_automovil_by_filter_db(filtro)
        return render_template('menu_automoviles.html', data=rows)
    return redirect(url_for('menu_automoviles'))


# These routes are for the CRUD operations of autos

@app.route("/menu/automoviles/eliminar/<int:id_automovil>", methods=['GET', 'POST'])
@login_required
def eliminar_automovil(id_automovil):
    if request.method == 'POST':        
        return redirect(url_for('menu_automoviles'))
    return redirect(url_for('menu_automoviles'))


@app.route("/menu/automoviles/agregar", methods=['GET', 'POST'])
@login_required
def crear_automovil():    
    if request.method == 'POST':    
        return redirect(url_for('menu_automoviles'))
    return redirect(url_for('menu_automoviles'))

@app.route("/menu/automoviles/modificar/<int:id_automovil>", methods=['GET', 'POST'])
@login_required
def actualizar_automovil(id_automovil):
    if request.method == 'POST':        
        return redirect(url_for('menu_automoviles'))
    return redirect(url_for('menu_automoviles'))

