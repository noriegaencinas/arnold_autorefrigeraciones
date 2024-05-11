from main import app

from controller.login_controller import *

from model.empleado_model import *

# Menu empelados

@app.route("/menu/empleados")
@app.route("/menu/empleados/page")
@app.route("/menu/empleados/page/<int:page>")
@login_required
def menu_empleados(page=1):
    rows = select_empleados_db(page)
    return render_template('menu_empleados.html', empleados=rows)

@app.route("/menu/empleados/eliminar/<int:id_empleado>", methods=['GET', 'POST'])
@login_required
def eliminar_empleado(id_empleado):
    if request.method == 'POST':
        eliminar_empleado_id(id_empleado)
        return redirect(url_for('menu_empleados'))
    return redirect(url_for('menu_empleados'))


@app.route("/menu/empleados/agregar", methods=['GET', 'POST'])
@login_required
def crear_empleado():    
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        cargo = request.form['cargo']
        fecha_contratacion = request.form['fecha_contratacion']
        activo = 1
        horario_trabajo = request.form['horario_trabajo']
        numero_contacto = request.form['numero_contacto']
        correo_electronico = request.form['correo_electronico']
        salario = request.form['salario']
        agregar_empleado_db(nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario)
        return redirect(url_for('menu_empleados'))
    return redirect(url_for('menu_empleados'))

@app.route("/menu/empleados/modificar/<int:id_empleado>", methods=['GET', 'POST'])
@login_required
def actualizar_empleado(id_empleado):
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        cargo = request.form['cargo']
        fecha_contratacion = request.form['fecha_contratacion']
        activo = 1
        horario_trabajo = request.form['horario_trabajo']
        numero_contacto = request.form['numero_contacto']
        correo_electronico = request.form['correo_electronico']
        salario = request.form['salario']
        actualizar_empleado_db(id_empleado, nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario)
        return redirect(url_for('menu_empleados'))
    return redirect(url_for('menu_empleados'))