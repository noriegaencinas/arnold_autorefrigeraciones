from main import app

from model.factura_empleado_model import *

from flask import render_template, request
# Menu facturas

@app.route("/menu/facturas/")
def menu_facturas_clientes():    
    return render_template('menu_facturas_clientes.html')