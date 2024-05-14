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

@app.route("/menu/inventario/agregar", methods=['GET', 'POST'])
@login_required
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        tipo= request.form['tipo']
        descripcion = request.form['descripcion']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        crear_producto_db( nombre, cantidad, precio_compra, tipo, descripcion, precio_venta)
        return redirect(url_for('menu_inventario'))
    return redirect(url_for('menu_inventario'))

@app.route("/menu/inventario/modificar/<int:id_inventario>", methods=['GET', 'POST'])
@login_required
def actualizar_producto(id_inventario):
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        tipo= request.form['tipo']
        descripcion = request.form['descripcion']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        actualizar_producto_db(id_inventario, nombre, cantidad, precio_compra, tipo, descripcion, precio_venta)
        return redirect(url_for('menu_inventario'))
    return redirect(url_for('menu_inventario'))

@app.route("/menu/inventario/eliminar/<int:id_inventario>", methods=['GET', 'POST'])
@login_required
def eliminar_producto(id_inventario):
    if request.method == 'POST':
        eliminar_producto_db(id_inventario)   
        return redirect(url_for('menu_inventario'))
    return redirect(url_for('menu_inventario'))   

@app.route("/menu/inventario/buscar", methods=['GET', 'POST'])
@login_required
def select_producto_by_filter():
    if request.method == 'POST':
        filtro = request.form['filtro']
        rows = select_producto_by_filter_db(filtro)
        return render_template('menu_inventario.html', data=rows)
    return redirect(url_for('menu_inventario'))
